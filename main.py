import pixela_graphs
import pixela_pixels
import pixela_users
from defines import *


def main():
    if __name__ == "__main__":
        uses_list = [
            "create_user",
            "create_graph",
            "modify_graph",
            "create_pixel_today",
            "addto_pixel_today",
            "quit",
        ]

        print("Options:\n")
        for use in uses_list:
            print(f"{use} [{uses_list.index(use)}]")
        current_use_index = int(input("\t"))
        current_use = uses_list[current_use_index]

        # Generate Pixela user #
        if current_use == uses_list[0]:
            pixela_users.create_user()
            # https://pixe.la/@lhgs
        #########################

        # Generate a graph
        elif current_use == uses_list[1]:
            pixela_graphs.create_graph()
            # https://pixe.la/v1/users/lhgs/graphs/d0loc0graph.html
        #########################

        # Update Graph
        elif current_use == uses_list[2]:
            pixela_graphs.modify_graph()
        #########################

        # Generate a day pixel
        elif current_use == uses_list[3]:
            quantity = input("how many for the pixel:\n\t")
            pixela_pixels.create_pixel(quantity)
        #########################

        # Add to a day pixel
        elif current_use == uses_list[4]:
            quantity = input("how many to add to the pixel\n\t")
            pixela_pixels.add_to_pixel(quantity)
        #########################

        elif current_use == uses_list[5]:
            return
        else:
            return

        print("https://pixe.la/v1/users/lhgs/graphs/d0loc0graph.html")


main()
