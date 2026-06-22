import pixela_graphs
import pixela_pixels
import pixela_users


def main():
    if __name__ == "__main__":
        uses_list = [
            "",
            "User Actions",
            "Graph Actions",
            "Pixel Actions",
            "quit",
        ]

        print("Options:\n")
        for use in uses_list[1:]:
            print(f"{use} [{uses_list.index(use)}]")
        current_use = int(input("\t"))

        # Generate Pixela user #
        if current_use == 1:
            pixela_users.chose_user_acttion()
            # https://pixe.la/@lhgs
        #########################

        # Generate a graph
        elif current_use == 2:
            pixela_graphs.chose_graph_action()
            # https://pixe.la/v1/users/lhgs/graphs/d0loc0graph.html
        #########################

        # Generate a day pixel
        elif current_use == 3:
            pixela_pixels.chose_pixel_action()
        #########################

        elif current_use == 4:
            return
        else:
            return

        print("https://pixe.la/v1/users/lhgs/graphs/d0loc0graph.html")


main()
