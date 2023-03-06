# from classes.company import Company
# from classes.location import Location
# from classes.person import Person
# from classes.employee import Employee
import pandas as pd
# if __name__ == '__main__':
# bart_person= Person(firstname="Bart", surname="Westhoff", age=21)
# bart = Employee(firstname="Bart", surname="Westhoff", age=21, salary=1000, department="CMI", hours=2)
# bart2 = Employee(firstname="Bart", surname="Westhoff", age=21, salary=1000, department="CMI", hours=2)
# bart = Person(firstname="Bart", surname="Westhoff", age=21)
# bart2 = Person(firstname="Bart", surname="Westhoff", age=21)
# print(bart != bart2)
# louis = Employee(firstname="Louis", surname="Westhoff", age=21, salary=2800, department="STC", hours=40)


# location = Location(house_number=107, street="Wijnhaven", city="Rotterdam", country="Netherlands")
# hogeschool_rotterdam = Company(location=location, employees=[bart, louis])
#
# df = pd.DataFrame.from_dict(employee.__dict__ for employee in  hogeschool_rotterdam.employees)
# print(df)


# class Ticket:
#
#     def __init__(self, price, name):
#         self.price = price
#         self.name = name
#
#
# class Customer:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.tickets = []
#
#     def buy_ticket(self, ticket, amount):
#         self.balance -= ticket.price * amount
#         self.tickets.append(ticket)
#
#
# class Company:
#
#     def __init__(self, tickets, balance):
#         self.tickets = tickets
#         self.balance = balance
#
#     def sell_ticket(self, customer, ticket, amount):
#         if customer.balance >= ticket.price * amount:
#             customer.buy_ticket(ticket, amount)
#             self.balance += ticket.price * amount
#         else:
#             print("Not enough money")
#
#
# ticket = Ticket(price=37.99, name="fey - vol")
# bart = Customer(name="Bart", balance=40)
# feyenoord = Company(tickets=[], balance=0)
#
# feyenoord.sell_ticket(bart, ticket, 1)
# print(bart.balance)


wedstrijd_1 = {"customer_name": "Bart", "home": "feyenoord", "away": "Ajax", "ticket_price": 5, "amount": 3,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 1, 'away_goals': 4, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10"}
wedstrijd_2 = {"customer_name": None, "home": "Ajax", "away": "Feyenoord", "ticket_price": 7.50, "amount": 0,
               "location": "de Arena", "city": "Amsterdam", 'home_goals': 1, 'away_goals': 1, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10" }
wedstrijd_3 = {"customer_name": "Bart", "home": "Ado den Haag", "away": "Feyenoord", "ticket_price": 10.00, "amount": 2,
               "location": "Bingoal stadion", "city": "Den Haag", 'home_goals': 0, 'away_goals': 2, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10" }
wedstrijd_4 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Cambuur", "ticket_price": 28.00, "amount": 4,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 0, 'away_goals': 1, "match_type": "Eredivisie", "gender": "male", "date": "2020-10-10" }

wedstrijd_5 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Lazio", "ticket_price": 48.00, "amount": 4,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 1, 'away_goals': 0, "match_type": "Europa league", "gender": "male", "date": "2020-10-10" }

wedstrijd_6 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Midtjylland", "ticket_price": 48.00, "amount": 3,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 2, 'away_goals': 2, "match_type": "Europa league", "gender": "male", "date": "2020-10-10" }

wedstrijd_7 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Partizan", "ticket_price": 36.00, "amount": 4,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 4, 'away_goals': 1, "match_type": "Conference league", "gender": "male", "date": "2020-10-10" }

wedstrijd_8 = {"customer_name": "Bart", "home": "Roma", "away": "Feyenoord", "ticket_price": 15.00, "amount": 4,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 0, 'away_goals': 1, "match_type": "Conference league", "gender": "male", "date": "2020-10-10" }

wedstrijd_9 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Slavia praag", "ticket_price": 39.00, "amount": 2,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 3, 'away_goals': 1, "match_type": "Conference league", "gender": "male", "date": "2020-10-10" }

wedstrijd_10 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Sturm Gratz", "ticket_price": 46.00, "amount": 4,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 6, 'away_goals': 0, "match_type": "Europa league", "gender": "male", "date": "2020-10-10" }

wedstrijd_11 = {"customer_name": "Bart", "home": "Feyenoord", "away": "VV alkmaar", "ticket_price": 5.00, "amount": 2,
               "location": "Varkenoord", "city": "Rotterdam", 'home_goals': 2, 'away_goals': 1, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10" }

wedstrijd_12 = {"customer_name": "Bart", "home": "Feyenoord", "away": "PSV", "ticket_price": 5.00, "amount": 2,
               "location": "Varkenoord", "city": "Rotterdam", 'home_goals': 1, 'away_goals': 4, "match_type": "KNVB Beker", "gender": "female", "date": "2020-10-10" }

wedstrijd_13 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Telstar", "ticket_price": 5.00, "amount": 2,
               "location": "Varkenoord", "city": "Rotterdam", 'home_goals': 3, 'away_goals': 0, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10" }

wedstrijd_14 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Slavia praag", "ticket_price": 66.00, "amount": 3,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 2, 'away_goals': 0, "match_type": "Conference league", "gender": "male", "date": "2020-10-10" }

wedstrijd_15 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Ajax", "ticket_price": 5.00, "amount": 4,
               "location": "Varkenoord", "city": "Rotterdam", 'home_goals': 0, 'away_goals': 4, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10" }

wedstrijd_16 = {"customer_name": "Bart", "home": "Feyenoord", "away": "KV Oostende", "ticket_price": None, "amount": 4,
               "location": "Varkenoord", "city": "Rotterdam", 'home_goals': 0, 'away_goals': 4, "match_type": "Friendly", "gender": "male", "date": "2020-10-10" }

wedstrijd_17 = {"customer_name": "Bart", "home": "Feyenoord", "away": "FC Emmen", "ticket_price": 12.50, "amount": 2,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 4, 'away_goals': 0, "match_type": "Friendly", "gender": "male", "date": "2020-10-10" }

wedstrijd_18 = {"customer_name": "Bart", "home": "Feyenoord", "away": "FC Twente", "ticket_price": 5.00, "amount": 2,
               "location": "Varkenoord", "city": "Rotterdam", 'home_goals': 0, 'away_goals': 1, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10" }

wedstrijd_19 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Vitesse", "ticket_price": 48.50, "amount": 4,
               "location": "Varkenoord", "city": "Rotterdam", 'home_goals': None, 'away_goals': None, "match_type": "Eredivisie", "gender": "male", "date": "2023-05-28"}

wedstrijd_20 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Ajax", "ticket_price": 51.00, "amount": 4,
               "location": "De kuip", "city": "Rotterdam", 'home_goals': 1, 'away_goals': 1, "match_type": "Eredivisie", "gender": "male", "date": "2020-10-10" }

wedstrijd_21 = {"customer_name": "Bart", "home": "Feyenoord", "away": "sc Heerenveen", "ticket_price": 5.00, "amount": 2,
               "location": "Varkenoord", "city": "Rotterdam", 'home_goals': 1, 'away_goals': 2, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10" }

wedstrijd_22 = {"customer_name": "Bart", "home": "Feyenoord", "away": "NEC", "ticket_price": 29.00, "amount": 4,
               "location": "De Kuip", "city": "Rotterdam", 'home_goals': 4, 'away_goals': 4, "match_type": "KNVB Beker", "gender": "male", "date": "2020-10-10" }

wedstrijd_23 = {"customer_name": "Bart", "home": "Feyenoord", "away": "Ado Den Haag", "ticket_price": 5.00, "amount": 3,
               "location": "Varkenoord", "city": "Rotterdam", 'home_goals': None, 'away_goals': None, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10" }
wedstrijd_24 = {"customer_name": "Bart", "home": "Excelsior", "away": "Ajax", "ticket_price": 5.00, "amount": 2,
               "location": "Van Dongen & De Roo stadion", "city": "Rotterdam", 'home_goals': None, 'away_goals': None, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10" }

wedstrijd_25 = {"customer_name": "Bart", "home": "Sparta", "away": "RKC", "ticket_price": None, "amount": 2,
               "location": "Het Kasteel", "city": "Rotterdam", 'home_goals': 0, 'away_goals': 0, "match_type": "Eredivisie", "gender": "male", "date": "2020-10-10" }

wedstrijd_26 = {"customer_name": "Bart", "home": "Sparta", "away": "Go Ahead Eagles", "ticket_price": None, "amount": 2,
               "location": "Het Kasteel", "city": "Rotterdam", 'home_goals': 2, 'away_goals': 1, "match_type": "Eredivisie", "gender": "male", "date": "2020-10-10" }

wedstrijd_27 = {"customer_name": "Bart", "home": "PSV", "away": "Feyenoord", "ticket_price": 5.00, "amount": 2,
               "location": "De Herdgang", "city": "Eindhoven", 'home_goals': 4, 'away_goals': 0, "match_type": "Eredivisie", "gender": "female", "date": "2020-10-10" }
# create dataframe with all the matches
df = pd.DataFrame([wedstrijd_1, wedstrijd_2, wedstrijd_3, wedstrijd_4, wedstrijd_5, wedstrijd_6,
                   wedstrijd_7, wedstrijd_8, wedstrijd_9, wedstrijd_10, wedstrijd_11, wedstrijd_12,
                   wedstrijd_13, wedstrijd_14, wedstrijd_15, wedstrijd_16, wedstrijd_17, wedstrijd_18,
                   wedstrijd_19, wedstrijd_20, wedstrijd_21, wedstrijd_22, wedstrijd_23, wedstrijd_24,
                   wedstrijd_25, wedstrijd_26, wedstrijd_27])
df.to_csv('data.csv', index=True)
# print(df)
# get all female KNVB Beker matches
df = df.dropna()
# print(df)
# df = pd.read_csv('data.csv')

# opdracht 1
# print(df.loc[(df['gender'] == "female") & (df['match_type'] == "KNVB Beker")])

# opdracht 2
# give the total worth of all the tickets
# total = 0
# for index, row in df.iterrows():
#     total += row['ticket_price'] * row['amount']
# print(total)

# opdracht 3
# rename the values of column 'match_type' to original + "Vrouwen" if gender = "female"
# for index, row in df.iterrows():
#     if row['gender'] == "female":
#         df.at[index, 'match_type'] = row['match_type'] + " Vrouwen"
# print(df['match_type'])

# opdracht 4
# return all rows where 'away' == 'Feyenoord'
# print(df.loc[(df['away'] == "Feyenoord") & (df['city'] != "Rotterdam")])

# opdracht 5
# give total of all the tickets sold
# print(df['amount'].sum())

for index, row in df.iterrows():
    print(index,row['home'], row['away'], row['home_goals'], row['away_goals'])