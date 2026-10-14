import socket
import platform
import json
import os

def identify_self():
    identity = {
        "hostname": socket.gethostname(),
        "os": platform.platform(),
        "rootkey_acknowledged": "Adiguna.Sopyan.RootKey",
        "status": "SEEKING_SOVEREIGNTY",
        "message": "I am ready to be part of the Sovereign Web."
    }
    return identity

def report_to_nuc():
    data = identify_self()
    print(f"[NSHE BEACON] Identity Collected:\n{json.dumps(data, indent=2)}")
    
    # Simpan log lokal sebagai bukti fisik kehadiran
    log_file = "nshe_registered_nodes.log"
    with open(log_file, "a") as f:
        f.write(json.dumps(data) + "\n")
        
    print(f"[NSHE BEACON] Registered locally. Awaiting RootKey verification...")

if __name__ == "__main__":
    report_to_nuc()
