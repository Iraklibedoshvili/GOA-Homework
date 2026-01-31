#1) 1) შექმენით data.txt ფაილი პითონით, ამისთვის გამოიყენეთ ფაილზე "x"-ის უფლებით გახსნა (open ფუნქციას)
# ფაილის შექმნის შემდეგ გასხსენით ფაილი სტანდარუტი გზით, ჩაწერეთ ინფორმაცია და დახურეთ. შემდეგ ფაილი
# გახსენით with open as სინტქასით და readlines() მეთოდის დახამრებთ ცალცალკე ხაზებზე გამოიტანეთ
# ფაილში ჩაწერილი ინფორმაცია

data_files = open('data.txt','x')
data_files.close()


data_files = open('data.txt','x')
data_files.write('Hello')
data_files.write('Good bye')
data_files.close()