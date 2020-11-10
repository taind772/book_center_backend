import document.services as DocumentServices


def search_document_by_title(title, first=0, limit=20):
    documents = DocumentServices.document_by_title(title=title)[first: first + limit]
    return {
        'has_next': len(documents) == limit,
        'documents': documents
    }


def search_document_by_year(year: int, first=0, limit=20):
    documents = DocumentServices.document_by_year(year=year)[first: first + limit]
    return {
        'has_next': len(documents) == limit,
        'documents': documents
    }



def search_document_by_language(language: str, first=0, limit=20):
    documents = DocumentServices.document_by_language(language=language)[first: first + limit]
    return {
        'has_next': len(documents) == limit,
        'documents': documents
    }


def document_filter(title=None, year=None, language=None, category=None, first=0, limit=20):
    documents = DocumentServices.document_filter(title=title, year=year, language=language, category=category)[first: first + limit]
    return {
        'has_next': len(documents) == limit,
        'documents': documents
    }