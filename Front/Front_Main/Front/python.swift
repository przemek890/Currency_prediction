import Foundation

func run_python_script(currency: String, date_start: String, date_end: String) {
    let task = Process()
    task.executableURL = URL(fileURLWithPath: "/bin/bash")

    let pythonScriptPath = "/Users/przemek899/Desktop/currency_prediction/swift.py"
    let virtualenvPath = "/Users/przemek899/Desktop/currency_prediction/venv/bin/python"

    task.currentDirectoryPath = "/Users/przemek899/Desktop/currency_prediction"

    let script = """
                 \(virtualenvPath) \(pythonScriptPath) \(currency) \(date_start) \(date_end)
                 """

    task.arguments = ["-c", script]

    let pipe = Pipe()
    task.standardOutput = pipe

    task.launch()

    let data = pipe.fileHandleForReading.readDataToEndOfFile()

    task.waitUntilExit()
}
