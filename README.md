# Cinema ticket system
Cinema ticket system built with Svelte, Python with FastAPI and MongoDB.
## Configuration
Enter your MongoDB connection string and your randomly generated SECRET_KEY in ```back/src/secret.py```. You can generate your secret key using OpenSSL.
```
openssl rand -hex 32
```
You also need to set your API URL in ```front/src/lib/constants/constants.svelte```
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