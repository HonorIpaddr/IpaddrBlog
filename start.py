from blogApp import app
app=app.create_app()
if __name__ == '__main__':
	app.run(host="localhost",port=5000)