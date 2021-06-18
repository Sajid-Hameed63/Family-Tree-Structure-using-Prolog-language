from pyswip import Prolog

class Prolog_Interface:
    prolog = None
    def __init__ (self):
        self.prolog = Prolog()
        self.prolog.consult("PROLOG (1).pl")
    def run_query(self,qury):
        return self.prolog.query(qury)
    def print_family_members(self):
        print("\t\t\t\t\t The family members of KHAN FAMILY are \n")
        print("\t\t\t chotekhan\tbarrekhan\tsalim\tnadir\tasad\trizwan\tburhan \n\t\t\t rashid\takram\tchotirani\tbarrirani\tkauser\tnahid\tsumra \n\t\t\t\t\t\t sanam\tsalima\trabia \n")
    def print_menu(self):
        print("\t\t\t 1. baap(X,Y)        2. gins(X,Y)    3. parents(X,Y)      4. maa(X,Y)")
        print("\t\t\t 5. beta(X,Y)        6. beti(X,Y)    7. dada(X,Y)         8. dadi(X,Y)")
        print("\t\t\t 9. nana(X,Y)        10. nani(X,Y)   11. pota(X,Y)        12. poti(X,Y)")
        print("\t\t\t 13. sala(X,Y)       14. sali(X,Y)   15. bahu(X,Y)        16. nawasa(X,Y)")
        print("\t\t\t 17. nawasi(X,Y)     18. sassur(X,Y) 19. chachataya(X,Y)  20. khala(X,Y)")
        print("\t\t\t 21. baapdada(X,Y)")
    def select_query(self):
        print("\t\t\t\t\t ----------------------")
        print("\t \t\t\t\t WELCOME TO KHAN FAMILY")
        print("\t\t\t\t\t ----------------------")
        print()
        self.print_family_members()
        print("\t\t\t\t\t Follwing are the facts \n")
        print("\t\t\t 1 mianbiwi(fact1,fact2) 2 parent(fact1,fact2) 3 gins(fact1,fact2)")
        print()
        print("\t\t\t Below are all the queries that you can perform on KHANn FAMILY ")
        print("\t\t\t Please Select number to perform respective query from the given menu\n\n")
        self.print_menu()
        print()
        qry = int(input("Please Enter your query number to perfom  "))
        print()
        if qry == 1:
            qry = int(input("\t\t baap(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "baap("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "baap(X ,"+ qry +")"
            elif qry == 3:
                return "baap(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "baap("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 2:
            qry = int(input("\t\t gins(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "gins("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "gins(X,"+ qry +")"
            elif qry == 3:
                return "gins(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "gins("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 3:
            qry = int(input("\t\t parents(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "parents("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "parents(X,"+ qry +")"
            elif qry == 3:
                return "parents(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "parents("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 4:
            qry = int(input("\t\t maa(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "maa("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "maa(X,"+ qry +")"
            elif qry == 3:
                return "maa(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "maa("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 5:
            qry = int(input("\t\t beta(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "beta("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "beta(X,"+ qry +")"
            elif qry == 3:
                return "beta(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "beta("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 6:
            qry = int(input("\t\t beti(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "beti("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "beti(X,"+ qry +")"
            elif qry == 3:
                return "beti(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "beti("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 7:
            qry = int(input("\t\t dada(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "dada(" + qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "dada(X," + qry +")"
            elif qry == 3:
                return "dada(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "dada("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 8:
            qry = int(input("\t\t dadi(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "dadi(" + qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "dadi(X,"+ qry +")"
            elif qry == 3:
                return "dadi(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "dadi("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 9:
            qry = int(input("\t\t nana(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "nana("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "nana(X,"+ qry +")"
            elif qry == 3:
                return "nana(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "nana("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 10:
            qry = int(input("\t\t nani(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "nani(" + qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "nani(X,"+ qry +")"
            elif qry == 3:
                return "nani(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "nani("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 11:
            qry = int(input("\t\t pota(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "pota("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "pota(X,"+ qry +")"
            elif qry == 3:
                return "pota(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "pota("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 12:
            qry = int(input("\t\t poti(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "poti("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "poti(X,"+ qry +")"
            elif qry == 3:
                return "poti(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "poti("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 13:
            qry = int(input("\t\t sala(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "sala("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "sala(X,"+ qry +")"
            elif qry == 3:
                return "sala(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "sala("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 14:
            qry = int(input("\t\t sali(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "sali("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "sali(X,"+ qry +")"
            elif qry == 3:
                return "sali(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "sali("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 15:
            qry = int(input("\t\t bahu(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "bahu("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "bahu(X,"+ qry +")"
            elif qry == 3:
                return "bahu(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "bahu("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 16:
            qry = int(input("\t\t nawasa(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "nawasa("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "nawasa(X,"+ qry +")"
            elif qry == 3:
                return "nawasa(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "nawasa("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 17:
            qry = int(input("\t\t nawasi(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "nawasi("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "nawasi(X,"+ qry +")"
            elif qry == 3:
                return "nawasi(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "nawasi("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 18:
            qry = int(input("\t\t sassur(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "sassur("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "sassur(X,"+ qry +")"
            elif qry == 3:
                return "sassur(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "sassur("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 19:
            qry = int(input("\t\t chachataya(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "chachataya("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "chachataya(X,"+ qry +")"
            elif qry == 3:
                return "chachataya(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "chachataya("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 20:
            qry = int(input("\t\t khala(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "khala("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "khala(X,"+ qry +")"
            elif qry == 3:
                return "khala(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "khala("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        elif qry == 21:
            qry = int(input("\t\t baapdada(X,Y) for X enter 1 , for Y enter 2 and for tree enter 3, for checking the relaton please enter 4 "))
            if qry == 1:
                self.print_family_members()
                qry = input("\t\t Enter the member name for X ")
                return "baapdada("+ qry +",Y)"
            elif qry == 2:
                self.print_family_members()
                qry = input("\t\t Enter the member name for Y ")
                return "baapdada(X,"+ qry +")"
            elif qry == 3:
                return "baapdada(X,Y)"
            elif qry == 4:
                arg_one = input("\t\t Enter the member name for X ")
                arg_two = input("\t\t Enter the member name for Y ")
                return "baapdada("+ arg_one +","+ arg_two +")"
            else:
                return "Invalid Choice"
        else:
            return "Invalid Choice"
def main():
    pl_int = Prolog_Interface()
    res = pl_int.select_query()
    if res == "Invalid Choice":
        print(res)
    else:
        res = list(pl_int.run_query(res))
        if res[0] == {}:
            print("The relation is valid")
        elif len(res) == 0:
            print("The relation is not valid")
        else:
            print(res)
if __name__ == "__main__":
    main()
