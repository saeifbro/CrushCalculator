


# Crush calculater potanor Licence checker


class UnderAgeToLoveError (Exception):
    pass
class BrokeBoyError (Exception):
    pass
class NotRomanticEnoughError(Exception):
    pass



age=int(input("Enter you age: "))
Balance=int(input("Enter your Balance you have: "))
Romantic_Level=int(input("Enter your Level:  "))

try:
    if(age<18):
        raise UnderAgeToLoveError("❌ ভাই, আগে বড় হ। প্রেম করার লাইসেন্স নাই এখনো।")

    if(Balance<5000):
        raise  BrokeBoyError("❌ টাকাই নাই, কই দিয়ে প্রেম করবি? 😢")

    if(Romantic_Level<10):
      raise   NotRomanticEnoughError("❌ প্রেম মানে শুধু ফুল না ভাই, ফিলিংসও লাগে।")

    else:
        print("✅ বাহ বাহ! লাইসেন্স দেওয়া হইলো। পটানোর ট্রাই দিয়া দে ভাই! ❤️")




except UnderAgeToLoveError as e:
    print(e)

except BrokeBoyError as e:
    print(e)
except NotRomanticEnoughError as e:
    print(e)

except ValueError as e:
    print("❌ ভাই, সংখ্যায় ইনপুট দে! প্রেমে ভুল চলবে না।")


finally:
    print("😎 Crush Calculator চালিয়ে যাও... আশা ছাড়িস না!")




class Student:
    def __int__(self,name,marks):
        self.name=name
        self.marks=marks





s1=Student("saeif")