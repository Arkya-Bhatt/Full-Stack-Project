import reflex as rx

from ..ui.base import base_page

from . import state

# @rx.page(route="/about-us")

def blog_post_detail_page() -> rx.Component:
    can_edit = True
    edit_link = rx.link("Edit", href=f"{state.BlogPostState.blog_post_edit_url}")
    edit_link_el = rx.cond(
        can_edit,
        edit_link,
        rx.fragment(""),
    )
    my_child = rx.vstack(
            rx.hstack(
                rx.heading(state.BlogPostState.post.title, size="9"),
                # rx.text(state.BlogPostState.blog_post_id),
                edit_link_el,
                align="end",
            ),
            rx.text(state.BlogPostState.post.publish_date,),
            rx.text(
                state.BlogPostState.post.content,
                white_space="pre-wrap",
            ),
            spacing="5",
            # justify="center",
            align="center",
            min_height="85vh",
            # id="my-child",
        )
    return base_page(my_child)