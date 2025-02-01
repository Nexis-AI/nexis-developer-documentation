# Install the Nexis Network Tool Suite

## Install the Nexis Network Tool Suite

There are multiple ways to install the Nexis Network tools on your computer depending on your preferred workflow:

* Use Nexis Network Install Tool
* MacOS & Linux
* Windows
* Download Prebuilt Binaries
* Linux
* MacOS
* Windows
* Build From Source

### Use Nexis Network Install Tool

#### MacOS & Linux

* Open your favorite Terminal application
* Install the Nexis Network release LATEST\_Nexis Network\_RELEASE on your machine by running:

```
curl -sSf https://raw.githubusercontent.com/Nexisnetwork/Nexis-network-blockchain/develop/install/Nexisnetwork-install-init.sh | sh -s - LATEST_NexisNETWORK_RELEASE
```

* &#x20;If you are connecting to a different testnet, you can replace `LATEST_NexisNETWORK_RELEASE` with the release tag matching the software version of your desired testnet, or replace it with the named channel `stable`, `beta`, or `edge`.
* The following output indicates a successful update:

```
looking for latest release downloading LATEST_NexisNETWORK_RELEASE installer
Configuration: /home/Nexisnetwork/.config/Nexisnetwork/install/config.yml
Active release directory: /home/Nexisnetwork/.local/share/Nexisnetwork/install/active_release
```



\* Release version: LATEST\_NexisNETWORK\_RELEASE



\* Release URL: https://github.com/Nexisnetwork /Nexis-network-blockchain/releases/download/LATEST\_NexisNETWORK\_RELEASE/Nexisnetwork-release-x86\_64-unknown-linux-gnu.tar.bz2



Update successful

* Depending on your system, the end of the installer messaging may prompt you to

Please update your PATH environment variable to include the Nexis Network programs:

* If you get the above message, copy and paste the recommended command below it to update `PATH`

`export PATH="/root/.local/share/Nexisnetwork/install/active_release/bin:$PATH"` to `bashrc`

* Confirm you have the desired version of `Nexisnetwork` installed by running:

Nexisnetwork --version

* After a successful install, `Nexisnetwork-install update` may be used to easily update the Nexis Network software to a newer version at any time.

***

#### Windows

#### Open a Command Prompt (`cmd.exe`) as an Administrator

* Search for Command Prompt in the Windows search bar. When the Command Prompt app appears, right-click and select “Open as Administrator”. If you are prompted by a pop-up window asking “Do you want to allow this app to make changes to your device?”, click Yes.
* Copy and paste the following command, then press Enter to download the Nexis Network installer into a temporary directory:

```
curl -L https://github.com/Nexisnetwork/Nexisnetwork-chain/releases/download/v0.5.1/Nexisnetwork-install-init-x86_64-pc-windows-msvc.exe --output C:\Nexis-install-tmp\Nexis-install-init.exe --create-dirs
```

* Copy and paste the following command, then press Enter to install the latest stable version of Nexis Network. If you see a security pop-up by your system, please select to allow the program to run.

C:\Nexis-install-tmp\Nexis-install-init.exe stable

* &#x20;When the installer is finished, press Enter.
* Close the command prompt window and re-open a new command prompt window as a normal user
*
  * Search for "Command Prompt" in the search bar, then left click on the Command Prompt app icon, no need to run as Administrator)

·       Confirm you have the desired version of `Nexis` installed by entering:

```
Nexis --version
```

* After a successful install, `Nexis-install update` may be used to easily update the Nexis Network software to a newer version at any time.

### Download Prebuilt Binaries

If you would rather not use `Nexis-install` to manage the install, you can manually download and install the binaries.

#### Linux

Download the binaries by navigating to https://github.com/Nexisnetwork/Nexisnetwork-chain/releases/latest, download **Nexisnetwork-release-x86\_64-unknown-linux-msvc.tar.bz2**, then extract the archive:

```
tar jxf Nexis-release-x86_64-unknown-linux-gnu.tar.bz2
cd Nexis-release/
export PATH=$PWD/bin:$PATH
```

#### MacOS

Download the binaries by navigating to https://github.com/Nexisnetwork/Nexis-network-blockchain/releases/latest, download **Nexisnetwork-release-x86\_64-apple-darwin.tar.bz2**, then extract the archive:

```
tar jxf Nexis-release-x86_64-apple-darwin.tar.bz2
cd Nexis-release/
export PATH=$PWD/bin:$PATH
```

#### Windows

* Download the binaries by navigating to https://github.com/Nexisnetwork/Nexisnetwork-chain/releases/latest, download **Nexisnetwork-release-x86\_64-pc-windows-msvc.tar.bz2**, then extract the archive using WinZip or similar.
* &#x20;Open a Command Prompt and navigate to the directory into which you extracted the binaries and run:

```
cd Nexis-release/
set PATH=%cd%/bin;%PATH%
```

### Build From Source

If you are unable to use the prebuilt binaries or prefer to build it yourself from source, navigate to https://github.com/Nexisnetwork/Nexis-network-blockchain/releases/latest, and download the **Source Code** archive. Extract the code and build the binaries with:

```
./scripts/cargo-install-all.sh .
export PATH=$PWD/bin:$PATH
```
