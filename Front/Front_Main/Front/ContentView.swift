import SwiftUI
/////////////////
let currency_pairs = ["chfpln", "eurpln", "gbppln", "jpypln", "nokpln", "usdpln"]       // currency pairs to choose from

struct ContentView: View {
    @State private var selectedCurrencyPairs: [String] = []
    @State private var startDate = Date()
    @State private var endDate = Date()
    @State private var showAlert = false

    var body: some View {
        VStack(spacing: 20) {
            Text("An application supporting investments")
                    .font(.largeTitle)

            Divider()

            Text("Select a pair of currencies")
                    .font(.headline)

            HStack {
                ForEach(currency_pairs, id: \.self) { currencyPair in
                    Button(action: {
                        if selectedCurrencyPairs.contains(currencyPair) {
                            selectedCurrencyPairs.removeAll { $0 == currencyPair }
                        } else {
                            selectedCurrencyPairs.append(currencyPair)
                        }
                    }) {
                        Text(currencyPair)
                                .foregroundColor(selectedCurrencyPairs.contains(currencyPair) ? .white : .blue)
                                .padding()
                                .background(selectedCurrencyPairs.contains(currencyPair) ? Color.blue : Color.clear)
                                .cornerRadius(8)
                    }
                            .buttonStyle(PlainButtonStyle())
                }
            }

            Divider()

            Text("Select a date range")
                    .font(.headline)

            HStack {
                DatePicker("Starting date", selection: $startDate, displayedComponents: .date)
                        .labelsHidden()
                        .datePickerStyle(CompactDatePickerStyle())

                DatePicker("End date", selection: $endDate, displayedComponents: .date)
                        .labelsHidden()
                        .datePickerStyle(CompactDatePickerStyle())
            }

            Divider()

            Image("coin")
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 100, height: 100)

            Button(action: {
                DispatchQueue.global().async {
                    if !selectedCurrencyPairs.isEmpty && endDate >= startDate {
                        run_python_script(currency: selectedCurrencyPairs, date_start: format_date(date: startDate), date_end: format_date(date: endDate))
                    } else {
                        showAlert = true
                    }
                }
            }) {
                Text("Generate chart")
                        .foregroundColor(.white)
                        .padding()
                        .background(Color.blue)
                        .cornerRadius(8)
            }
                    .buttonStyle(PlainButtonStyle())
                    .alert(isPresented: $showAlert) {
                        Alert(title: Text("Error"), message: Text("Input mismatch error!"), dismissButton: .default(Text("OK")))
                    }
        }
                .frame(width: 1000, height: 500)
                .padding()
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
