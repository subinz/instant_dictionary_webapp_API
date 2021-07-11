import justpy as jp

class Doc:

    @classmethod
    def serve(cls, request):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant Dictionary API", classes="text-4xl m-2")
        jp.Div(a=div, text="Get definition of words:", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=moon \nor\n http://127.0.0.1:8000/api?w=moon", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="or", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="http://127.0.0.1:8000/api?w=moon", classes="text-lg")
        jp.Hr(a=div)
        jp.Hr(a=div)
        jp.Div(a=div, text="""{"word": "moon", 
        "definition": 
        ["A natural satellite of a planet.", 
        "A month, particularly a lunar month (approximately 28 days).", "To fuss over adoringly or with great affection.", 
        "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).". 
        "To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."]}
        """,)
        return wp
