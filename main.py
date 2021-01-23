from DBA import DBA
import re
if __name__ == '__main__':
    dba_con = DBA()
    number_of_postings_retrieve = dba_con.get_number_of_postings()
    print(number_of_postings_retrieve)

    # request again and retrieve new number and calculate delta 