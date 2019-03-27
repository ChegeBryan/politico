# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.14.1] - 2019-03-26

### Removed

- Unused imports in code

## [1.14.0] - 2019-03-26

### Added

- Version 2 of get all offices api route

### Changed

- Offices are queried from a database

## [1.13.0] - 2019-03-26

### Added

- Version 2 of get office api route
- Authorization for get office/offices route

### Changed

- Office is queried from a database
- Offices api requires authorization token
- Office json response now includes the office id
- Get office api route takes in integer as variable instead of uuid

## [1.12.0] - 2019-03-26

### Added

- Version 2 of Create office api route
- Authorization for create office route

### Changed

- Office created is saved to a database
- Creating an office requires admin authorization token
- Office name and office type are saved as lowercase by default

### Deprecated

- version 1 of offices api routes

## [1.11.0] - 2019-03-25

### Added

- Version 2 of delete party  api route
- Authorization for delete party

### Changed

- Party deleted is from a database
- Deleting a party requires admin authorization token
- Party id takes in integer instead of uuid variable

## [1.10.0] - 2019-03-25

### Added

- Version 2 of edit party name api route
- Authorization for edit party name

### Changed

- Party name edited is from a database
- Editing party name requires admin authorization token
- Party id takes in integer instead of uuid variable

## [1.9.0] - 2019-03-25

### Added

- Version 2 of get parties api route

### Changed

- Parties list is queried from database
- Party schema json response is ordered as per the schema fields

## [1.8.0] - 2019-03-24

### Added

- Version 2 of get party api route
- Authorization get parties api route

### Changed

- Parties list is queried from a database
- Getting party/parties requires authorization
- Party id takes in integer instead of uuid variable

## [1.7.0] - 2019-03-23

### Added

- Logo field attribute to parties details
- Version 2 of create party api route
- Authorization for parties v2 api

### Changed

- Parties to be stored in database
- To create a party it requires an admin user token

### Deprecated

- version 1 of parties api routes

### Removed

- Party id generated using uuid

## [1.6.0] - 2019-03-17

### Added

- Updated the CHANGELOG
- Updated the README

## [1.5.1] - 2019-03-17

### Fixed

- Removed unused imports on modules
- Unnecessary blank lines
- Code line length
- Whitespaces in modules.

## [1.5.0] - 2019-03-16

### Added

- Decorators to verify currently logged in user privileges

### Security

- Restrict access of route to specific class of users (normal or admin)

## [1.4.0] - 2019-03-15

### Added

- Logout route
- Blacklist table to store tokens when user logs out

## [1.3.1] - 2019-02-20

### Fixed

- Include PyJWT package in project requirements list

## [1.3.0] - 2019-02-20

### Added

- Jwt token encoding on user emails
- Jwt token decoding

### Changed

- JSON response for user login and registration included token field.

## [1.2.0] - 2019-02-19

### Added

- User login endpoint route
- Validation for user login details

## [1.1.1] - 2019-02-19

### Security

- Sanitized sql string queries

## [1.1.0] - 2019-02-16

### Added

- User registration endpoint
- Validation for user fields inputs
- PostgresSQL database connection

### Removed

- default set passport Url on user registration

## [1.0.0] - 2019-02-12

### Added

- Offices endpoints.
- Parties endpoints.
- Validated data for user inputs.
- Heroku deployment for this release.

[1.0.0]: https://github.com/ChegeBryan/politico/compare/gh-pages...develop
[1.1.0]: https://github.com/ChegeBryan/politico/compare/v1.0.0...v1.1.0
[1.1.0]: https://github.com/ChegeBryan/politico/compare/v1.1.0...v1.1.1
[1.2.0]: https://github.com/ChegeBryan/politico/compare/v1.1.1...v1.2.0
[1.3.0]: https://github.com/ChegeBryan/politico/compare/v1.2.0...v1.3.0
[1.3.1]: https://github.com/ChegeBryan/politico/compare/v1.3.0...v1.3.1
[1.4.0]: https://github.com/ChegeBryan/politico/compare/v1.3.1...v1.4.0
[1.5.0]: https://github.com/ChegeBryan/politico/compare/v1.4.0...v1.5.0
[1.5.1]: https://github.com/ChegeBryan/politico/compare/v1.5.0...v1.5.1
[1.6.0]: https://github.com/ChegeBryan/politico/compare/v1.5.1...v1.6.0
[1.7.0]: https://github.com/ChegeBryan/politico/compare/v1.6.0...v1.7.0
[1.8.0]: https://github.com/ChegeBryan/politico/compare/v1.7.0...v1.8.0
[1.9.0]: https://github.com/ChegeBryan/politico/compare/v1.8.0...v1.9.0
[1.10.0]: https://github.com/ChegeBryan/politico/compare/v1.9.0...v1.10.0
[1.11.0]: https://github.com/ChegeBryan/politico/compare/v1.10.0...v1.11.0
[1.12.0]: https://github.com/ChegeBryan/politico/compare/v1.11.0...v1.12.0
[1.13.0]: https://github.com/ChegeBryan/politico/compare/v1.12.0...v1.13.0
[1.14.0]: https://github.com/ChegeBryan/politico/compare/v1.13.0...v1.14.0
[1.14.1]: https://github.com/ChegeBryan/politico/compare/v1.14.0...v1.14.1
