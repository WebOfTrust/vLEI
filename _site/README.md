# Sparán

The KERI Wallet (Sparán) is a heavyweight wallet providing a GUI for managing local KERI identifiers and keys. It is built on top of the KERI library, a custom KERI agent runtime, and Flet, a Flutter-based application framework.

## Installation

Sparán uses the [uv][UV] build system, an extremely fast Python package and project manager written in Rust. See their [installation instructions][UV_INSTALL] to install it for your platform. 

These instructions show how to set it up on a Mac, and Linux should be similar.

### uv setup

You can run 

`make setup`

which does a `curl -LsSf https://astral.sh/uv/install.sh | sh` to install uv.

## Developing

To run a python command with the `uv` environment you do

- `uv run python <command/file>`

### Running Sparán

You can run the app locally with the KERI demo witnesses and the [vLEI-server][VLEI_SERVER] credential schema caching server.
See the [local services](#local-services) section for running the witnesses and `vLEI-server`. Start the local services prior to starting the wallet.

So to run the wallet you would do

- `uv run python main.py`

or run directly with flet, after installing all dependencies with `make setup`, as 

- `uv run flet run main.py`

If you want to run the wallet with the development environment you need to export the `WALLET_ENVIRONMENT` variable as `development` before running the wallet.

- `export WALLET_ENVIRONMENT=development; uv run flet run main.py` 

or `make dev`

### <a name="local-services"></a> Local Services

Running locally is intended to work with the sample set of six witnesses provided by the `kli witness demo` command.

Run the following two services prior to running Wallet, the witness pool and the vLEI server. You must run each from the respective root directories of each repository.

```bash
# In one terminal window run the following from the KERIpy repository
kli witness demo

# and in another terminal window run the following from the vLEI repository
vLEI-server -s ./schema/acdc -c ./samples/acdc/ -o ./samples/oobis/
```

### Other environments

Wallet allows configuration of the witnesses used, agent configuration directory, and inception
configuration file with the following environment variables. You can also specify only
WALLET_ENVIRONMENT and the other  variables will all be set to valid values.

#### Environment Toggle
- `WALLET_ENVIRONMENT`: production, staging, or development

#### Changing the environment for a deployed Wallet app bundle

To change the environment of a deployed Wallet app bundle add the following LSEnvironment key and the corresponding dict of environment variables to the `wallet.app/Contents/Info.plist` file:
```xml
<plist>
  ...
  <key>LSEnvironment</key>
  <dict>
    <key>WALLET_ENVIRONMENT</key>
    <string>development</string>
  </dict>
  ...
</plist>
```

#### Configuration Overrides

- `WITNESS_POOL_PATH`: Path to a JSON file containing key value pairs where the key is the
  pool name and the value is an array of witnesses.
- `KERI_CONFIG_DIR`: Path to a directory containing agent configuration including the
  bootstrap configuration file specified with the next environment variable.
- `KERI_AGENT_CONFIG_FILE`: The environment variable specifying the name only of the
  agent configuration file.

#### Staging

You do not need to run witnesses or the vLEI server locally for testing with staging because they are already running. Set a few variables to point to staging and then run Wallet.

```bash
export WALLET_ENVIRONMENT=staging

uv run python main.py
```

#### Production

Since the default config uses production then you just run Wallet.

```bash
uv run python main.py
```

Run the app normally. The default is to use the production


#### Signing

In order to package the application for release you must sign two things

1. The libsodium libraries in `./libsodium` using `./sign-libs.sh`
2. The application bundle using `./sign.sh`

This process prepares the application bundle for installation on macOS. This requires an Apple Account and a local installation of developer signing certificates through Xcode.

See the process to add a keychain item for stored credentials using app specific passwords https://developer.apple.com/documentation/security/customizing-the-notarization-workflow

Add a new keychain item for signing:

```
xcrun notarytool store-credentials "org.example.foo"
--apple-id "<AppleID>"
--team-id <DeveloperTeamID>
--password <secret_2FA_password>
```

Run `sign.sh`

```
export WALLET_ENVIRONMENT="development"; export DEVELOPER_ID_APP_CERT="Developer ID Application: YOUR_ID_HERE"; make sign
```

`DEVELOPER_ID_APP_CERT` can be found using `security find-identity -p basic`

## Contributing

### Code style and formatting

We use [ruff][RUFF] to format the code, an extremely fast Python code formatter written in Rust.

See editor integration: https://docs.astral.sh/ruff/editors/setup/ or `make fmt`




---

[RUFF]: https://github.com/astral-sh/ruff
[UV]: https://docs.astral.sh/uv/
[UV_INSTALL]: https://docs.astral.sh/uv/getting-started/installation/
[VLEI_SERVER]: https://github.com/WebOfTrust/vLEI