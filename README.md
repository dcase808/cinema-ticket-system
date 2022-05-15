# Cinema ticket system
Cinema ticket system built with Svelte, Python with FastAPI and MongoDB.
## Configuration
Enter your MongoDB connection string in ```back/src/db_connect.py``` and enter your randomly generated SECRET_KEY in ```back/src/auth.py```. You can generate it using OpenSSL.
```
openssl rand -hex 32
```
## Running application
### Run front-end application
Enter ```front``` folder and install all dependencies.
```
npm install
```
Then run application in development mode.
```
npm run dev
```
Or run application in production mode.
```
npm run build
```

### Run API
Enter ```back/src``` folder and install all dependencies.
```
pip install -r requirements.txt
```
Run API using uvicorn server.
```
uvicorn main:app --reload
```