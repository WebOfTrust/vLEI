import multiprocessing
import os
import signal
import time

import requests

from vlei import server


def wait_for_server(port, timeout=10):
    """Poll server until it responds or until timeout"""
    url=f"http://127.0.0.1:{port}/health"
    start_time=time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True # Server is up
        except requests.ConnectionError:
            pass # Server not ready yet
        time.sleep(0.25) # Retry every 1/4 second
    return False # Timeout

def test_shutdown_signals():
    config = server.VLEIConfig(http=9999)

    # Test SIGTERM
    vlei_process = multiprocessing.Process(target=server.launch, args=[config])
    vlei_process.start()
    assert wait_for_server(config.http), "vLEI-server did not start as expected."

    os.kill(vlei_process.pid, signal.SIGTERM)  # Send SigTerm to the process, signal 15
    vlei_process.join(timeout=10)
    assert not vlei_process.is_alive(), "SIGTERM: vLEI-server process did not shut down as expected."
    assert vlei_process.exitcode == 0, f"SIGTERM: vLEI-server exited with non-zero exit code {vlei_process.exitcode}"

    # Test SIGINT
    vlei_process = multiprocessing.Process(target=server.launch, args=[config])
    vlei_process.start()
    assert wait_for_server(config.http), "Agency did not start as expected."

    os.kill(vlei_process.pid, signal.SIGINT)  # Sends SigInt to the process, signal 2
    vlei_process.join(timeout=10)
    assert not vlei_process.is_alive(), "SIGINT: vLEI-server process did not shut down as expected."
    assert vlei_process.exitcode == 0, f"SIGINT: vLEI-server exited with non-zero exit code {vlei_process.exitcode}"
