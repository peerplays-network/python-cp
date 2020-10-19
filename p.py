from peerplays import PeerPlays

try:
    p1 = PeerPlays(node="ws://96.46.49.1:8090")
    print("p1", "success")
except Exception as e:
    print(e, "p1", "failed")


try:
    p2 = PeerPlays(node="ws://96.46.49.2:8090")
    print("p2", "success")
except Exception as e:
    print(e, "p2", "failed")

try:
    p3 = PeerPlays(node="ws://96.46.49.3:8090")
    print("p3", "success")
except Exception as e:
    print(e, "p3", "failed")

try:
    p4 = PeerPlays(node="ws://96.46.49.4:8090")
    print("p4", "success")
except Exception as e:
    print(e, "p4", "failed")

try:
    p5 = PeerPlays(node="ws://96.46.49.5:8090")
    print("p5", "success")
except Exception as e:
    print(e, "p5", "failed")

try:
    p6 = PeerPlays(node="ws://96.46.49.6:8090")
    print("p6", "success")
except Exception as e:
    print(e, "p6", "failed")

try:
    p7 = PeerPlays(node="ws://96.46.49.7:8090")
    print("p7", "success")
except Exception as e:
    print(e, "p7", "failed")

try:
    p8 = PeerPlays(node="ws://96.46.49.8:8090")
    print("p8", "success")
except Exception as e:
    print(e, "p8", "failed")

try:
    p9 = PeerPlays(node="ws://96.46.49.9:8090")
    print("p9", "success")
except Exception as e:
    print(e, "p9", "failed")

try:
    p10 = PeerPlays(node="ws://96.46.49.10:8090")
    print("p10", "success")
except Exception as e:
    print(e, "p10", "failed")

try:
    p11 = PeerPlays(node="ws://96.46.49.11:8090")
    print("p11", "success")
except Exception as e:
    print(e, "p11", "failed")

try:
    p12 = PeerPlays(node="ws://96.46.49.12:8090")
    print("p12", "success")
except Exception as e:
    print(e, "p12", "failed")

try:
    p13 = PeerPlays(node="ws://96.46.49.13:8090")
    print("p13", "success")
except Exception as e:
    print(e, "p13", "failed")

try:
    p14 = PeerPlays(node="ws://96.46.49.14:8090")
    print("p14", "success")
except Exception as e:
    print(e, "p14", "failed")

try:
    p15 = PeerPlays(node="ws://96.46.49.15:8090")
    print("p15", "success")
except Exception as e:
    print(e, "p15", "failed")

try:
    p16 = PeerPlays(node="ws://96.46.49.16:8090")
    print("p16", "success")
except Exception as e:
    print(e, "p16", "failed")


def SyncMeasure():
    try:
        info = p1.info()
        print("p1", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p1", "failed")
    try:
        info = p2.info()
        print("p2", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p2", "failed")
    try:
        info = p3.info()
        print("p3", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p3", "failed")
    try:
        info = p4.info()
        print("p4", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p4", "failed")
    try:
        info = p5.info()
        print("p5", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p5", "failed")
    try:
        info = p6.info()
        print("p6", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p6", "failed")
    try:
        info = p7.info()
        print("p7", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p7", "failed")
    try:
        info = p8.info()
        print("p8", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p8", "failed")
    try:
        info = p9.info()
        print("p9", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p9", "failed")
    try:
        info = p10.info()
        print("p10", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p10", "failed")
    try:
        info = p11.info()
        print("p11", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p11", "failed")
    try:
        info = p12.info()
        print("p12", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p12", "failed")
    try:
        info = p13.info()
        print("p13", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p13", "failed")
    try:
        info = p14.info()
        print("p14", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p14", "failed")
    try:
        info = p15.info()
        print("p15", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p15", "failed")
    try:
        info = p16.info()
        print("p16", info["head_block_number"], info[
            "last_irreversible_block_num"])
    except Exception as e:
        print(e, "p16", "failed")
