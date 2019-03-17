# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
