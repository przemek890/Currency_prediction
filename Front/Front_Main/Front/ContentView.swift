import SwiftUI

struct ContentView: View {
    @State private var selectedCurrencyPair = "chfpln"

    var body: some View {
        VStack {
            Text("Investing App")
                    .font(.largeTitle)
                    .padding()

            Image("dogecoin.png") // Użyj nazwy odpowiedniego obrazka
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 200, height: 200)

            Picker("Wybierz parę walut", selection: $selectedCurrencyPair) {
                Text("CHF/PLN").tag("chfpln")
                Text("EUR/PLN").tag("eurpln")
                Text("GBP/PLN").tag("gbppln")
                Text("JPY/PLN").tag("jpypln")
                Text("NOK/PLN").tag("nokpln")
                Text("USD/PLN").tag("usdpln")
            }
                    .pickerStyle(SegmentedPickerStyle())
                    .padding()

            Button(action: {
                // Tutaj możesz dodać kod do generowania wykresów
            }) {
                Text("Generuj wykresy")
                        .font(.headline)
                        .padding()
                        .background(Color.blue)
                        .foregroundColor(.white)
                        .cornerRadius(10)
            }

            Spacer()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}