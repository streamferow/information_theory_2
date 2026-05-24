"""
Flask API for Channel Capacity Calculator
Provides REST endpoints for frontend integration
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from calculator import ChannelParams, calculate_channel_capacity, generate_chart_data

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access


@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """
    Calculate channel capacity
    
    Request body: {"N": 1000, "P": 0.01, "M": 0.05}
    Response: {"success": true, "data": {...}} or {"success": false, "error": "..."}
    """
    try:
        data = request.get_json()
        
        N = float(data.get('N', 1000))
        P = float(data.get('P', 0.01))
        M = float(data.get('M', 0.05))
        
        params = ChannelParams(N=N, P=P, M=M)
        result, error = calculate_channel_capacity(params)
        
        if error:
            return jsonify({"success": False, "error": error}), 400
        
        return jsonify({
            "success": True,
            "data": result.to_dict()
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/chart', methods=['POST'])
def api_chart():
    """
    Generate chart data
    
    Request body: {"N": 1000, "M": 0.05}
    Response: {"success": true, "data": [...]}
    """
    try:
        data = request.get_json()
        
        N = float(data.get('N', 1000))
        M = float(data.get('M', 0.05))
        
        chart_data = generate_chart_data(N, M)
        
        return jsonify({
            "success": True,
            "data": chart_data
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/info', methods=['GET'])
def api_info():
    """Get API information"""
    return jsonify({
        "name": "Channel Capacity Calculator API",
        "version": "1.0",
        "endpoints": {
            "/api/calculate": "POST - Calculate channel capacity",
            "/api/chart": "POST - Generate chart data",
            "/api/info": "GET - API information"
        }
    })


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    print("=" * 60)
    print("  Channel Capacity Calculator API")
    print("  Starting server on http://localhost:5000")
    print("=" * 60)
    print()
    app.run(host='0.0.0.0', port=5000, debug=True)
