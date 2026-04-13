"# Test Credentials for Giri & Associates CA Platform

## Admin Account
Use Google OAuth for admin login. Any Google account can be registered as admin by setting role='admin' in the database after first login.

## Client Account
Use Google OAuth for client login. Default role is 'client'.

## Manual Test Session (for testing agent)
Run the mongosh command from auth_testing.md to create a test session token.

## Test Data
- Service IDs will be generated on first seed
- Document upload paths: giriasocc/uploads/{user_id}/{uuid}.{ext}
"