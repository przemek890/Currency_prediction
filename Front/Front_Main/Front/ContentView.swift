import SwiftUI

struct ContentView: View {
    let currencyPairs = ["chfpln", "eurpln", "gbppln", "jpypln", "nokpln", "usdpln"]
    @State private var selectedCurrencyPair: String?
    @State private var startDate = Date()
    @State private var endDate = Date()

    var body: some View {
        VStack(spacing: 20) {
            Text("Aplikacja wspomagająca inwestycje")
                    .font(.largeTitle)

            Divider()

            Text("Wybierz parę walut")
                    .font(.headline)

            HStack {
                ForEach(currencyPairs, id: \.self) { currencyPair in
                    Button(action: {
                        selectedCurrencyPair = currencyPair
                    }) {
                        Text(currencyPair)
                                .foregroundColor(selectedCurrencyPair == currencyPair ? .white : .blue)
                                .padding()
                                .background(selectedCurrencyPair == currencyPair ? Color.blue : Color.clear)
                                .cornerRadius(8)
                    }
                            .buttonStyle(PlainButtonStyle())
                }
            }

            Divider()

            Text("Wybierz zakres dat")
                    .font(.headline)

            HStack {
                DatePicker("Data początkowa", selection: $startDate, displayedComponents: .date)
                        .labelsHidden()
                        .datePickerStyle(CompactDatePickerStyle())

                DatePicker("Data końcowa", selection: $endDate, displayedComponents: .date)
                        .labelsHidden()
                        .datePickerStyle(CompactDatePickerStyle())
            }

            Divider()

            Button(action: {
                // Tutaj dodaj logikę generowania wykresu dla danej pary walut
            }) {
                Text("Generuj wykres")
                        .foregroundColor(.white)
                        .padding()
                        .background(Color.blue)
                        .cornerRadius(8)
            }
                    .buttonStyle(PlainButtonStyle())

            Spacer()
        }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
                .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
