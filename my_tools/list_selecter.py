
class list_select:


    @staticmethod

    def find_all(list, condition):
        """)
        :param list:
        :param condition:
        :return:
        """
        for item in list:
            if condition(item):
                yield item



    @staticmethod
    def find_first_one(list, condition):
        """)
        :param list:
        :param condition:
        :return:
        """
        for item in list:
            if condition(item):
                return item


    @staticmethod
    def select_info(list01,condiction):
        for item in list01:
            yield condiction(item)


    @staticmethod
    def count(list01,condiction):
        sum = 0
        for item in list01:
            sum += condiction(item)
        return sum

    @staticmethod
    def find_last_one(list, condition):
        """

        :param list:
        :param condition:
        :return:
        """
        a=''
        for item in list:
            if condition(item):
                a=item
        return a

    @staticmethod
    def condiction_count(list, condition):
        """)
        :param list:
        :param condition:
        :return:
        """

        count=0
        for item in list:
            if condition(item):
                count+=1
        return count

    @staticmethod
    def judge_one(list, condition):
        """)
        :param list:
        :param condition:
        :return:
        """
        for item in list:
            if condition(item):
                return True

        return False

    @staticmethod

    def delete_all(list, condition):
        """)
        :param list:
        :param condition:
        :return:
        """
        for item in list:
            if condition(item):
                list.remove(item)
        for item in list:
                yield item

    @staticmethod
    def find_max(list, condition):
        """
        :param list:
        :param condition:
        :return:
        """
        extream_for_now = 0
        for item in range(len(list)-1):
                if condition(list[item])>extream_for_now:
                    extream_for_now = condition(list[item])
        return  extream_for_now

    @staticmethod
    def sort_list_low_to_high(list, condition):
        """
        :param list:
        :param condition:
        :return:
        """
        list02=[]
        for item in list:
            list02.append(condition(item))
        list02.sort()

        return  list02

    @staticmethod
    def sort_list_high_to_low(list, condition):
        """
        :param list:
        :param condition:
        :return:
        """
        list02 = []
        for item in list:
            list02.append(condition(item))
        list02.sort()
        list02.reverse()

        return list02



    @staticmethod
    def sort_list(list, condition):
        """
        :param list:
        :param condition:
        :return:
        """
        list02 = []
        for item in range(len(list)-1):
            for c in range(item+1,len(list)):
                if condition(list[item],list[c]):
                    list[item],list[c]=list[c],list[item]


    @staticmethod
    def find_min(list, condition):
        """
        :param list:
        :param condition:
        :return:
        """
        extream_for_now = list[0]
        for item in range(len(list) - 1):
            if condition(list[item]) < condition(extream_for_now):
                extream_for_now = condition(list[item])
        return extream_for_now