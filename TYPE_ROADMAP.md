
#### Session 1: Import and Define Missing Types
1. **Objective**: Ensure all necessary types are imported and defined. Do not quote type-hints!
2. **Steps**:
   - Review the import statements in each file and ensure all required types from `typing` (e.g., `List`, `Dict`, `Optional`, `Union`) are imported.
   - Define any custom types that are missing or unclear, such as `JsonData`, `AuthTokens`, etc.
   Notes: do not update code that is already correct

#### Session 2: Add Type Annotations to Functions
1. **Objective**: Add missing type annotations to functions. Do not quote type-hints!
2. **Steps**:
   - For each function missing type annotations, determine the expected input and output types.
   - Add type annotations to function signatures, including return types.
   - Example: `def my_function(param1: int, param2: str) -> bool:`
   - Notes: do not update code that is already correct

#### Session 3: Resolve 'Any' Type Issues
1. **Objective**: Replace `Any` types with specific types.  Do not quote type-hints!
2. **Steps**:
   - Identify variables and expressions currently typed as `Any`.
   - Determine the correct type for each and update the type annotations.
   - Use `mypy` to check for remaining `Any` types and iteratively refine.
   - Notes: do not update code that is already correct

#### Session 4: Fix Incompatible Type Assignments
1. **Objective**: Correct type mismatches in assignments. Do not quote type-hints!
2. **Steps**:
   - Review each error related to incompatible types in assignments.
   - Ensure the variable types match the assigned values.
   - Update variable types or cast values as necessary to resolve mismatches.
   - Notes: do not update code that is already correct

#### Session 5: Address Subscriptable Type Issues
1. **Objective**: Correct usage of non-subscriptable types. Do not quote type-hints!
2. **Steps**:
   - Replace instances of `list`, `dict`, etc., with `List`, `Dict`, etc., from `typing`.
   - Ensure all collections are properly typed using `typing` generics.
   - Notes: do not update code that is already correct

#### Session 6: Handle Attribute and Index Errors
1. **Objective**: Fix attribute and index errors. Do not quote type-hints!
2. **Steps**:
   - Review errors related to missing attributes or invalid index types.
   - Ensure objects have the expected attributes and are indexed correctly.
   - Update code logic to handle optional types safely.

#### Session 6: Handle Attribute and Index Errors
1. **Objective**: Fix attribute and index errors. Do not quote type-hints!
2. **Steps**:
   - Review errors related to missing attributes or invalid index types.
   - Ensure objects have the expected attributes and are indexed correctly.
   - Update code logic to handle optional types safely.
   - Notes: do not update code that is already correct

#### Session 7: Final Review and Testing
1. **Objective**: Ensure all typing issues are resolved and code is stable. Do not quote type-hints!
2. **Steps**:
   - Run `mypy` to verify all typing errors are resolved.
   - Conduct a code review to ensure type annotations are consistent and logical.
   - Test the application to ensure functionality is unaffected by type changes.
   - Notes: do not update code that is already correct
#### Session 4: Fix Incompatible Type Assignments
1. **Objective**: Correct type mismatches in assignments. Do not quote type-hints!
2. **Steps**:
   - Review each error related to incompatible types in assignments.
   - Ensure the variable types match the assigned values.
   - Update variable types or cast values as necessary to resolve mismatches.
