from flask import Flask, render_template
from com.ApplicationManager import ApplicationManager
from com.Docker import Docker
from com.DockerInfo import DockerInfo
from com.Container import Container

app = Flask(__name__)


@app.route('/fill')
def test1():
    applicationManager = ApplicationManager.getApplicationManager()
    dockerList = [Docker("hasan", DockerInfo("192.168.1.1", "Fail"))]
    applicationManager.setContainer("192.168.2.2", Container("192.168.2.2", dockerList))
    return render_template("robot.html", containerMap=applicationManager.getContainers())


@app.route('/list')
def test():
    applicationManager = ApplicationManager.getApplicationManager()
    containerMap = applicationManager.getContainers()
    return render_template("robot.html", containerMap=containerMap)


if __name__ == "__main__":
    app.run(debug=True)
