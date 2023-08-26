import Foundation

func run_python_script(currency: [String], date_start: String, date_end: String) {
    let task = Process()
    task.executableURL = URL(fileURLWithPath: "/bin/bash")                                          // system shell used

    let pythonScriptPath = "/Users/przemek899/Desktop/currency_prediction/swift.py"                 // path to swift.py file (The file must be in the main project directory)
    let virtualenvPath = "/Users/przemek899/Desktop/currency_prediction/venv/bin/python"            // path to python in virtual environment

    task.currentDirectoryPath = "/Users/przemek899/Desktop/currency_prediction"                     // path to the root directory of the project


    let currencyString = currency.joined(separator: "_")
    let script = """
                 \(virtualenvPath) \(pythonScriptPath) \(currencyString) \(date_start) \(date_end)
                 """

    task.arguments = ["-c", script]

    let pipe = Pipe()
    task.standardOutput = pipe

    task.launch()

    let data = pipe.fileHandleForReading.readDataToEndOfFile()

    task.waitUntilExit()
}
