from fastapi import FastAPI
from agents.utils import read_json

app = FastAPI()

RESULTS_PATH = 'kappa_results.json'


@app.get('/kappa')
def get_kappa():
    data = read_json(RESULTS_PATH, default=None)
    if not data:
        return {'kappa': None, 'date': None}
    entries = data.get('kappa_over_time', [])
    if not entries:
        return {'kappa': None, 'date': None}
    latest = entries[-1]
    return latest


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
