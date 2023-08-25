import Foundation

func run_python_script(currency: String, date_start: String, date_end: String) {
    let task = Process()
    task.executableURL = URL(fileURLWithPath: "/bin/bash")

    let pythonScriptPath = swiftpy_path
    let virtualenvPath = venv_python_path

    task.currentDirectoryPath = currency_prediction_path

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
