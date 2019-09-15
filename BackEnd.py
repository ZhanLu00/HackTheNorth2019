#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import requests
import random
import math
from utils import get_budget


# In[15]:


class Demographics:
    def __init__(self, age, income, relationship, habitation, region, school):
        self.age = age
        self.income = income
        self.relationship = relationship
        self.habitation = habitation
        self.region = region
        self.school = school


# In[60]:


class User:
    def __init__(self, ID):
        self.ID = ID
    
    def update_transaction(self):
        response = requests.get('https://api.td-davinci.com/api/customers/'+ self.ID +'/transactions',
        headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiZDNlNjI3ZTctYWE2Zi0zYTZmLTk5OTAtOWIyYjFhOTk0NjkwIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI0ODA4YjAzZi01YzhhLTQ2MmUtYTc4ZC02OGM2YWYwYzY1NDcifQ.S_BYKKXS7WB9sjWCU52cTsQcaWy_rkSIxCc5XfGikVg' })
        response_data = response.json()["result"]
        
        amount = []
        label = []
        trans_type = []
        for i in response_data:
            rand_num = random.randint(0, len(i.get('categoryTags'))-1)
            amount.append(i.get('currencyAmount'))
            label.append(i.get('categoryTags')[rand_num])
            trans_type.append(i.get('type'))
        
        trans_dict = dict()
        for i in range(0, len(label)):
            if label[i] in trans_dict.keys():
                orig_amount = (trans_dict[label[i]])[0]
                trans_dict[label[i]] = [orig_amount + amount[i], trans_type[i]]
            else:
                trans_dict[label[i]] = [amount[i], trans_type[i]]
        
        self.transaction = trans_dict
        
    def update_demographics(self):
        response_customer_info = requests.get('https://api.td-davinci.com/api/customers/' + self.ID,
        headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiZDNlNjI3ZTctYWE2Zi0zYTZmLTk5OTAtOWIyYjFhOTk0NjkwIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI0ODA4YjAzZi01YzhhLTQ2MmUtYTc4ZC02OGM2YWYwYzY1NDcifQ.S_BYKKXS7WB9sjWCU52cTsQcaWy_rkSIxCc5XfGikVg' })
        response_custinfo = response_customer_info.json()["result"]
        ID = response_custinfo.get('id')
        age = response_custinfo.get('age')
        if 'totalIncome' in response_custinfo:
            income = response_custinfo.get('totalIncome')
        else:
            income = 0;
        relationship_status = response_custinfo.get('relationshipStatus')
        habitation_status = response_custinfo.get('habitationStatus')
        region = (response_custinfo.get('addresses')).get('principalResidence').get('municipality')
        if 'schoolAttendance' in response_custinfo:
            school = response_custinfo.get("schoolAttendance")
        else:
            school = ''
        demographics = Demographics(age, income, relationship_status, habitation_status, region, school)
        self.demographics = demographics
        
    def update_total_cost(self):
        total_cost = 0
        for key in self.transaction:
            if key == 'Transfer' or key == 'Income':
                continue
            total_cost += abs((self.transaction[key])[0])
        self.total_cost = total_cost
    
    def update_total_income(self):
        total_income = self.demographics.income
        for key in self.transaction:
            if key == 'Income':
                total_income += abs((self.transaction[key])[0])
        self.total_income = total_income
        
    def product_recommend(self):
        diff = self.total_income - self.total_cost
        if diff >= 15000:
            product_name = 'TD Canadian Banking & Utilities GIC'
            GICtype = "Market Growth GIC"
            term = '3 years'
            avg_rate = '10.44%'
        elif diff >= 5000:
            product_name = 'TD Special Offer GICs'
            GICtype = 'Non-Cashable'
            if diff >= 10000:
                term = '18 months'
                avg_rate = '1.90%'
            else:
                term = '15 months'
                avg_rate = '1.12%'
        else:
            product_name = '100-Day TD Special Offer GIC'
            GICtype = 'Cashable'
            term = '100 days'
            avg_rate = '1.10%'
        gic = GIC(product_name, term, avg_rate, GICtype)
        self.gic = gic
    
    def budget_calculator(self):
        message_list = []
        for key in self.transaction:
            if key == 'Auto and Transport' and abs((self.transaction[key])[0]) > 0.15*self.total_income:
                message_list.append('Seems like you have travelled a lot, be careful on the road and also be careful about your wallet.')
            if key == 'Bills and Utilities' and abs((self.transaction[key])[0]) > 0.1*self.total_income:
                message_list.append('Don’t use too much energy, be nice to the earth')
            if key == 'Business Services' and abs((self.transaction[key])[0]) > 0.05*self.total_income:
                message_list.append('That’s too much for small function jobs! Be sure to find the right business function for you!')
            if key == 'Education':
                if self.demographics.age >= 24 and abs((self.transaction[key])[0]) > 0.05*self.total_income:
                    message_list.append('Take care of yourselves and your wallet. Don’t over push yourself for extra courses!')
                if self.demographics.age <= 16 and abs((self.transaction[key])[0]) > 0.05*self.total_income:
                    message_list.append('You should enjoy your childhood and teenager life, don\'t just spend time and money on courses!')
                if (self.demographics.age > 16 or self.demographics.age < 24) and abs((self.transaction[key])[0]) > 0.1*self.total_income:
                    message_list.append('Enjoy your spare time, it should be just built up with courses and workload!')
            if key == 'Entertainment' and abs((self.transaction[key])[0]) > 0.1*self.total_income:
                message_list.append('Be sure to work hard not just play hard!')
            if key == 'Fees and Charges' and abs((self.transaction[key])[0]) > 0.1*self.total_income:
                message_list.append('Think about how you can save something from all these bills.')
            if key == 'Financial' and abs((self.transaction[key])[0]) > 0.1*self.total_income:
                message_list.append('Choose the proper financial institution accordingly!')
            if key == 'Food and Dining' and abs((self.transaction[key])[0]) > 0.15*self.total_income:
                message_list.append('Be sure to enjoy what you want to eat and take care of the wallet as well!')
            if key == 'Gifts and Donation' and abs((self.transaction[key])[0]) > 0.01*self.total_income:
                message_list.append('Being nice to others is good, but make sure you can survive first!')
            if key == 'Health and Fitness' and abs((self.transaction[key])[0]) > 0.1*self.total_income:
                message_list.append('Go to the gym and enjoy, but be sure you can pay off the bill!')
            if key == 'Home' and abs((self.transaction[key])[0]) > 0.35*self.total_income:
                message_list.append('Be nice to your home but don’t spend way too much!')
            if key == 'Investments' and abs((self.transaction[key])[0]) > 0.1*self.total_income:
                message_list.append('Don’t be too risky on investments!')
            if key == 'Kids' and abs((self.transaction[key])[0]) > 0.15*self.total_income:
                    message_list.append('Don’t just get whatever your kids ask you to buy!')
            if key == 'Personal Care' and abs((self.transaction[key])[0]) > 0.1*self.total_income:
                message_list.append('Take care of your body condition and you can save some money too!')
            if key == 'Pets' and abs((self.transaction[key])[0]) > 0.05*self.total_income:
                message_list.append('Don’t feed your pets so well!')
            if key == 'Shopping' and abs((self.transaction[key])[0]) > 0.1*self.total_income:
                message_list.append('Don’t buy too many fancy staff, one or two should be fine!')
            if key == 'Travel' and abs((self.transaction[key])[0]) > 0.1*self.total_income:
                message_list.append('It’s nice to travel around but plan accordingly!')
        return message_list
            
    def budget_breakdown(self, budget):
        breakdown = dict()
        for key in self.transaction:
            if key == 'Income' or key == 'Transfer':
                continue
            month_budget = abs((self.transaction[key])[0])/self.total_cost*budget/12
            if key == 'Bills and Utilities' or key == 'Business Services' or key == 'Fees and Charges':
                if 'Service Fees' in breakdown.keys():
                    orig_amount = breakdown.get('Service Fees')
                    breakdown['Service Fees'] = orig_amount + abs((self.transaction[key])[0])
                else:
                    breakdown['Service Fees'] = abs((self.transaction[key])[0])
            elif key == 'Education':
                if 'Education' in breakdown.keys():
                    orig_amount = breakdown.get('Education')
                    breakdown['Education'] = orig_amount + abs((self.transaction[key])[0])
                else:
                    breakdown['Education'] = abs((self.transaction[key])[0])
            elif key == 'Entertainment' or key == 'Travel':
                if 'Entertainment' in breakdown.keys():
                    orig_amount = breakdown.get('Entertainment')
                    breakdown['Entertainment'] = orig_amount + abs((self.transaction[key])[0])
                else:
                    breakdown['Entertainment'] = abs((self.transaction[key])[0])
            elif key == 'Food and Dining':
                if 'Food' in breakdown.keys():
                    orig_amount = breakdown.get('Food')
                    breakdown['Food'] = orig_amount + abs((self.transaction[key])[0])
                else:
                    breakdown['Food'] = abs((self.transaction[key])[0])
            elif key == 'Gifts and Donations' or key == 'Health and Fitness' or key == 'Pets' or key == 'Personal Care' or key == 'Shopping':
                if 'Personal' in breakdown.keys():
                    orig_amount = breakdown.get('Personal')
                    breakdown['Personal'] = orig_amount + abs((self.transaction[key])[0])
                else:
                    breakdown['Personal'] = abs((self.transaction[key])[0])
            elif key == 'Home' or key == 'Kids':
                if 'Household' in breakdown.keys():
                    orig_amount = breakdown.get('Household')
                    breakdown['Household'] = orig_amount + abs((self.transaction[key])[0])
                else:
                    breakdown['Household'] = abs((self.transaction[key])[0])
            elif key == 'Financial' or key == 'Investment' or key == 'Loans' or key == 'Mortgage and Rent' or key == 'Taxes':
                if 'Financial' in breakdown.keys():
                    orig_amount = breakdown.get('Financial')
                    breakdown['Financial'] = orig_amount + abs((self.transaction[key])[0])
                else:
                    breakdown['Financial'] = abs((self.transaction[key])[0])
            elif key == 'Auto and Transportation':
                if 'Transportation' in breakdown.keys():
                    orig_amount = breakdown.get('Transportation')
                    breakdown['Transportation'] = orig_amount + abs((self.transaction[key])[0])
                else:
                    breakdown['Transportation'] = abs((self.transaction[key])[0])
            else:
                if 'Miscallaneous and Uncategorized' in breakdown.keys():
                    orig_amount = breakdown.get('Miscallaneous and Uncategorized')
                    breakdown['Miscallaneous and Uncategorized'] = orig_amount + abs((self.transaction[key])[0])
                else:
                    breakdown['Miscallaneous and Uncategorized'] = abs((self.transaction[key])[0])
        self.breakdown = breakdown


# In[61]:


class GIC: 
    def __init__(self, product_name, term, avg_rate, GICtype):
        self.product_name = product_name
        self.term = term
        self.avg_rate = avg_rate
        self.GICtype = GICtype


# In[66]:


user = User('ce16ef42-a4e8-41e0-8f45-1ccf3079b659')
user.update_transaction()
user.update_demographics()
user.update_total_cost()
user.update_total_income()


# In[67]:


def check_saving():
    if user.total_cost >= user.total_income:
        return 'Time to check all your bills, see how you can better survive for next year!'


# In[68]:


user.budget_calculator()
user.budget_breakdown(get_budget())
user.product_recommend()


# In[69]:


def print_product():
    message = 'Based on your previous purchase behavior, we will recommend you our '
    message += user.gic.product_name
    message += ', which is a '
    message += user.gic.GICtype
    message += ' ' + user.gic.term
    message += ' with the average yearly return rate of '
    message += user.gic.avg_rate
    return message

