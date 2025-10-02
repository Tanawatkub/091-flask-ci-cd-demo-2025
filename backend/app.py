from flask import Flask, jsonify
import os

# สร้าง Flask app
app = Flask(__name__)

# route หลัก
@app.route('/')
def hello():
    return jsonify({
        "message": "Hello World!",
        "status": "running"
    })

# route สำหรับ health check
@app.route('/health')
def health():
    # เช็คว่ามี environment variables สำหรับ DB/Redis หรือไม่
    db_status = "connected" if os.getenv('DATABASE_URL') else "not configured"
    redis_status = "connected" if os.getenv('REDIS_URL') else "not configured"
    
    return jsonify({
        "status": "healthy",
        "database": db_status,
        "redis": redis_status
    })

# จุดเริ่มต้นของแอป
if __name__ == '__main__':
    # host=0.0.0.0 ให้ container เรียกใช้จากภายนอกได้
    app.run(host='0.0.0.0', port=5000, debug=True)
