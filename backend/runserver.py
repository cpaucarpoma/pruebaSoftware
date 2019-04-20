from app import api
if __name__ == '__main__':
    api.app.run(host="localhost",port = 5000,debug=True)
    #api.manager.run()
    