import json
from helpers.handle_file import FileHandler


class DataAnalyzer:

    def __init__(self):
        self.fh = FileHandler()
        self.dict_of_requests = self.combine_data()

    def combine_data(self) -> dict:
        """
        Combines requests regarding IP. Returns requests for each IP.
        :return: dict
        """
        ordered_data = {}
        for line in self.fh.read_file():
            words = line.split()
            if words[0] not in ordered_data.keys():
                ordered_data.update({
                    f"{words[0]}": []
                })
            ordered_data[words[0]].append([words[5][1:], words[6], int(words[8]), int(words[9])])
        return ordered_data

    def count_general_num_of_requests(self) -> int:
        """
        Counts general number of requests.
        :return: int
        """
        return sum(self.amount_of_requests_by_method().values())

    def amount_of_requests_by_method(self) -> dict:
        """
        Returns number of requests by request method
        :return: dict
        """
        methods_dict = {}
        for value in self.dict_of_requests.values():
            for item in value:
                if item[0] not in methods_dict.keys():
                    methods_dict.update({
                        f"{item[0]}": 0
                    })
                methods_dict[item[0]] += 1
        return methods_dict

    def get_top_ten_ip_requests_made_from(self) -> dict:
        """
        Returns top ten of requests based on methods in a descending way
        :return: dict
        """
        requests_per_ip = {}
        for i in self.dict_of_requests:
            requests_per_ip.update({i: len(self.dict_of_requests[i])})
        return {k: v for k, v in sorted(requests_per_ip.items(), key=lambda item: item[1], reverse=True)[:10]}

    def get_top_ten_longest_requests(self) -> list:
        """
        Returns list of top ten [time, url, ip, method] sorting by time of execution in a descending way
        :return: list
        """
        requests_with_time = []
        for i in self.dict_of_requests:
            for value in self.dict_of_requests.values():
                for item in value:
                    requests_with_time.extend([[i, item[0], item[1], item[3]]])
        return [i for i in sorted(requests_with_time, key=lambda x: x[3], reverse=True)[:10]]

    def get_top_ten_requests_with_client_error(self) -> dict:
        """
        Returns dict of top ten [status_code, url, ip, method] for requests ended with client errors
        :return: dict
        """
        requests_with_client_error = {}
        for i in self.dict_of_requests:
            if i not in requests_with_client_error:
                requests_with_client_error.update({
                        f"{i}": []
                    })
            for value in self.dict_of_requests[i]:
                if value[2] in range(400, 500):
                    requests_with_client_error[i].append([value[0], value[1], value[2]])

        requests_with_number_of_client_error = {}
        for item in requests_with_client_error:
            if not requests_with_client_error[item]:
                continue
            requests_with_number_of_client_error.update({item: {f"{requests_with_client_error[item][0]}": 0}})
            for value in requests_with_client_error[item]:
                if str(value) not in requests_with_number_of_client_error[item].keys():
                    requests_with_number_of_client_error[item].update({str(value): 1})
                else:
                    requests_with_number_of_client_error[item][str(value)] += 1
        return requests_with_number_of_client_error

    def get_top_ten_requests_with_server_error(self) -> dict:
        """
        Returns dict of top ten [status_code, url, ip, method] for requests ended with server errors
        :return: dict
        """

        requests_with_server_error = {}
        for i in self.dict_of_requests:
            if i not in requests_with_server_error:
                requests_with_server_error.update({
                    f"{i}": []
                })
            for value in self.dict_of_requests[i]:
                if value[2] in range(500, 600):
                    requests_with_server_error[i].append([value[0], value[1], value[2]])

        requests_with_number_of_server_error = {}
        for item in requests_with_server_error:
            if not requests_with_server_error[item]:
                continue
            requests_with_number_of_server_error.update({item: {f"{requests_with_server_error[item][0]}": 0}})
            for value in requests_with_server_error[item]:
                if str(value) not in requests_with_number_of_server_error[item].keys():
                    requests_with_number_of_server_error[item].update({str(value): 1})
                else:
                    requests_with_number_of_server_error[item][str(value)] += 1

        return requests_with_number_of_server_error

        # Makes list without counting number of requests
        #
        # return requests_with_number_of_client_error
        # requests_with_server_error = []
        # for i in self.dict_of_requests:
        #     for value in self.dict_of_requests[i]:
        #         if value[2] in range(500, 600):
        #             requests_with_server_error.extend([[i, value[0], value[1], value[2]]])
        # return requests_with_server_error[:10]

    def report_maker(self):
        statistic_template = {
            "general_amount_of_requests": self.count_general_num_of_requests(),
            "amount_of_requests_by_method": self.amount_of_requests_by_method(),
            "top_ten_ip_requests_made_from": self.get_top_ten_ip_requests_made_from(),
            "top_ten_longest_requests": self.get_top_ten_longest_requests(),
            "top_ten_requests_with_client_error": self.get_top_ten_requests_with_client_error(),
            "top_ten_requests_with_server_error": self.get_top_ten_requests_with_server_error()
        }
        return json.dumps(statistic_template)
