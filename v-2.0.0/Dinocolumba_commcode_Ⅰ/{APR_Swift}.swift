import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 啟動 Dinocolumba_commcode.py
        runPythonScript(scriptName: "Dinocolumba_commcode.py")
        
        // 延遲 3 秒
        DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
            // 啟動 automate.py
            self.runPythonScript(scriptName: "app.py")
        }
    }
    
    func runPythonScript(scriptName: String) {
        if let pythonPath = Bundle.main.path(forResource: "python3", ofType: nil) {
            let task = Process()
            task.executableURL = URL(fileURLWithPath: pythonPath)
            task.arguments = [scriptName]
            
            do {
                try task.run()
            } catch {
                print("Error running Python script: \(error)")
            }
        } else {
            print("Python interpreter not found.")
        }
    }
}
