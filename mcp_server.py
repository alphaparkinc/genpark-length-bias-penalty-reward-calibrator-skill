import sys
import json
from client import LengthBiasRewardCalibrator

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-length-bias-penalty-reward-calibrator-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "calibrate_reward",
                        "description": "Subtracts length bias penalty from raw reward score",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "raw_reward": {"type": "number"},
                                "length": {"type": "integer"},
                                "target_length": {"type": "integer", "default": 150},
                                "alpha": {"type": "number", "default": 0.002}
                            },
                            "required": ["raw_reward", "length"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        name = params.get("name")
        args = params.get("arguments", {})
        
        if name == "calibrate_reward":
            res = LengthBiasRewardCalibrator.calibrate_reward(
                args.get("raw_reward", 0.0),
                args.get("length", 0),
                args.get("target_length", 150),
                args.get("alpha", 0.002)
            )
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
            
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def run():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    run()
