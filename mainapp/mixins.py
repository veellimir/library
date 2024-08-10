class StrMixin:
    def __str__(self):
        if hasattr(self, "name"):
            return self.name
        elif hasattr(self, "title"):
            return self.title
        elif hasattr(self, "book"):
            return self.book.title
        return super().__str__()
