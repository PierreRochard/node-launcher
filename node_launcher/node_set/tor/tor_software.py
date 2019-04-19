import os

from node_launcher.constants import (
    IS_WINDOWS,
    IS_MACOS,
    IS_LINUX,
    TARGET_WINDOWS_TOR_VERSION,
    TARGET_TOR_RELEASE
)
from node_launcher.node_set.lib.software import Software


class TorSoftware(Software):
    release_version = TARGET_TOR_RELEASE
    windows_version = TARGET_WINDOWS_TOR_VERSION
    software_name = 'tor'

    def __init__(self):
        super().__init__()
        if IS_MACOS:
            self.compressed_suffix = '.dmg'
            self.download_name = f'TorBrowser-{self.release_version}-osx64_en-US'
            self.downloaded_bin_path = os.path.join(
                self.binary_directory_path,
                'Tor Browser.app',
                'Contents',
                'MacOS',
                'Tor'
            )
        elif IS_LINUX:
            self.compressed_suffix = '.tar.xz'
            self.download_name = f'tor-browser-linux64-{self.release_version}_en-US'
        elif IS_WINDOWS:
            self.download_name = f'tor-win64-{self.windows_version}'
            self.downloaded_bin_path = os.path.join(self.binary_directory_path,
                                                    'Tor')

        self.download_url = f'http://www.torproject.org/dist/torbrowser/' \
            f'{self.release_version}/{self.download_destination_file_name}'

    @property
    def tor(self) -> str:
        name = 'tor.real'
        if IS_WINDOWS:
            name = 'tor.exe'
        latest_executable = os.path.join(self.static_bin_path, name)
        return latest_executable
