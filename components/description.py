import dash_mantine_components as dmc


def description(text_lst, className):

    dmc_text_lst = [dmc.Text(text, className="p-pb") for text in text_lst[:-1]]
    dmc_text_lst.append(dmc.Text(text_lst[-1]))

    return dmc.Card(
        dmc_text_lst,
        withBorder=True,
        radius="md",
        className=className,
    )
