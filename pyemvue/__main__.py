# CRITICAL: Do not quote type hints in this file. This applies to all future AI and developers. Type hints MUST NOT be quoted.

import sys
import datetime
import dateutil

# Our files
from pyemvue.device import VueDevice, VueUsageDevice
from pyemvue.types import DeviceUsageMap
from typing import Dict, List, Union
from pyemvue.enums import Scale, Unit
from pyemvue.pyemvue import PyEmVue


def print_recursive(
    usage_dict: DeviceUsageMap,
    info: Dict[int, VueDevice],
    scaleBy: float = 1,
    unit: str = "kWh",
    depth: int = 0,
) -> None:
    for gid, device in usage_dict.items():
        for channelnum, channel in device.channels.items():
            name = channel.name or "Unknown"
            if name == "Main":
                name = info.get(gid, VueDevice()).device_name
            usage = channel.usage or 0
            print("-" * depth, f"{gid} {channelnum} {name} {usage*scaleBy} {unit}")
            if channel.nested_devices:
                print_recursive(
                    channel.nested_devices,
                    info,
                    scaleBy=scaleBy,
                    unit=unit,
                    depth=depth + 1,
                )


def main() -> None:
    errorMsg = 'Please pass a file containing the "email" and "password" as json.'
    if len(sys.argv) == 1:
        print(errorMsg)
        sys.exit(1)

    filepath = sys.argv[1]
    vue = PyEmVue()
    vue.login(token_storage_file=filepath)
    print("Logged in. Authtoken follows:")
    print(vue.auth.tokens["id_token"])
    print()
    channelTypes = vue.get_channel_types()
    devices = vue.get_devices()
    deviceGids: List[int] = []
    deviceInfo: Dict[int, VueDevice] = {}
    for device in devices:
        if device.device_gid not in deviceGids:
            deviceGids.append(device.device_gid)
            deviceInfo[device.device_gid] = device
            print(
                device.device_gid, device.manufacturer_id, device.model, device.firmware
            )
            for chan in device.channels:
                channelTypeInfo = next(
                    (
                        c
                        for c in channelTypes
                        if c.channel_type_gid == chan.channel_type_gid
                    ),
                    None,
                )
                print(
                    "\t",
                    chan.device_gid,
                    chan.name,
                    chan.channel_num,
                    chan.channel_multiplier,
                    (
                        channelTypeInfo.description
                        if channelTypeInfo
                        else chan.channel_type_gid
                    ),
                )
        else:
            deviceInfo[device.device_gid].channels += device.channels
            for chan in device.channels:
                channelTypeInfo = next(
                    (
                        c
                        for c in channelTypes
                        if c.channel_type_gid == chan.channel_type_gid
                    ),
                    None,
                )
                print(
                    "\t",
                    chan.device_gid,
                    chan.name,
                    chan.channel_num,
                    chan.channel_multiplier,
                    (
                        channelTypeInfo.description
                        if channelTypeInfo
                        else chan.channel_type_gid
                    ),
                )

    monthly, start = vue.get_chart_usage(
        devices[0].channels[0], scale=Scale.MONTH.value
    )
    print(monthly[0], "kwh used since", start.isoformat())
    now = datetime.datetime.now(datetime.timezone.utc)
    midnight = (
        datetime.datetime.now(dateutil.tz.gettz(devices[0].time_zone))
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .astimezone(dateutil.tz.tzutc())
    )
    yesterday = midnight - datetime.timedelta(days=1)
    yesterday = yesterday.replace(tzinfo=None)
    print("Total usage for today in kwh: ")

    use = vue.get_device_list_usage(deviceGids, now, Scale.DAY.value)
    print_recursive(use, deviceInfo)
    print("Total usage for yesterday in kwh: ")
    for gid, device in deviceInfo.items():
        for chan in device.channels:
            usage = vue.get_chart_usage(
                chan,
                yesterday,
                yesterday + datetime.timedelta(hours=23, minutes=59),
                Scale.DAY.value,
            )
            if usage and usage[0]:
                print(f"{chan.device_gid} ({chan.channel_num}): {usage[0][0]} kwh")
    print("Average usage over the last minute in watts: ")
    use = vue.get_device_list_usage(deviceGids, None, Scale.MINUTE.value)
    print_recursive(use, deviceInfo, scaleBy=60000, unit="W")

    usage_over_time, start_time = vue.get_chart_usage(
        devices[0].channels[0],
        datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7),
        datetime.datetime.now(datetime.timezone.utc),
        scale=Scale.DAY.value,
        unit=Unit.KWH.value,
    )

    print("Usage for the last seven days starting", start_time.isoformat())
    for usage in usage_over_time:
        print(usage, "kwh")

    (outlets, chargers) = vue.get_devices_status(devices)
    print("List of Outlets:")
    for outlet in outlets:
        print(f"\t{outlet.device_gid} On? {outlet.outlet_on}")

    print("List of Chargers:")
    for charger in chargers:
        print(
            f"\t{charger.device_gid} On? {charger.charger_on} Charge rate: {charger.charging_rate}/{charger.max_charging_rate} Status: {charger.status}"
        )

    try:
        vehicles = vue.get_vehicles()
        print("List of Vehicles")
        for vehicle in vehicles:
            print(
                f"\t{vehicle.vehicle_gid} ({vehicle.display_name}) - {vehicle.year} {vehicle.make} {vehicle.model}"
            )

        print("List of Vehicle Statuses")
        for vehicle in vehicles:
            vehicleStatus = vue.get_vehicle_status(vehicle.vehicle_gid)
            if vehicleStatus:
                print(
                    f"\t{vehicleStatus.vehicle_gid} {vehicleStatus.vehicle_state} - Charging: {vehicleStatus.charging_state} Battery level: {vehicleStatus.battery_level}"
                )
            else:
                print(f"\t{vehicle.vehicle_gid} - No status available")
    except Exception as e:
        print(f"Error getting vehicles: {e}")


if __name__ == "__main__":
    main()
