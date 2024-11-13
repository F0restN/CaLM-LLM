from typing import List


class pubmed_instance:

    title: str = ""
    url: str = ""
    doi: str = ""
    pmid: str = ""
    authors: List[str] = []
    published_date: str = ""  # YYYY-mm-dd
    abstract: str = ""
    contents: str = ""
    per_sections_content: List[str] = []  # exclude reference from this section
    reference: str = ""

    def __init__(self, pmid="", url="", title="", doi="", published_date="",
                 abstract="", contents="", per_sections_content=None, reference="", authors=[]):
        self.title = title
        self.pmid = pmid
        self.doi = doi
        self.authors = authors
        self.published_date = published_date
        self.url = url

        # @TODO: add more information
        self.abstract = abstract
        self.contents = contents
        self.per_sections_content = per_sections_content if per_sections_content is not None else []
        self.reference = reference

    def __str__(self):
        return f"PMID: {self.pmid}\nTitle: {self.title}\nDOI: {self.doi}\nPublished Date: {self.published_date}\nAbstract: {self.abstract}\nContents: {self.contents}\nPer Sections Content: {self.per_sections_content}\nReference: {self.reference}"

    def __repr__(self):
        return f"PMID: {self.pmid}\nTitle: {self.title}\nDOI: {self.doi}\nPublished Date: {self.published_date}\nAbstract: {self.abstract}\nContents: {self.contents}\nPer Sections Content: {self.per_sections_content}\nReference: {self.reference}"

    def __dict__(self):
        return {
            "pmid": self.pmid,
            "url": self.url,
            "title": self.title,
            "doi": self.doi,
            "published_date": self.published_date,
            "abstract": self.abstract,
            "contents": self.contents,
            "per_sections_content": self.per_sections_content,
            "reference": self.reference
        }

    def self_report(self):
        # print missing information
        missing_list = self.self_missing_report()
        if len(missing_list) > 0:
            print(f"Missing information: {missing_list}")
        else:
            print("All information is complete.")
        print(self.__str__())

    def self_missing_report(self):
        missing_list = []
        if self.pmid == "":
            missing_list.append("pmid")
        if self.url == "":
            missing_list.append("url")
        if self.title == "":
            missing_list.append("title")
        if self.doi == "":
            missing_list.append("doi")
        if self.published_date == "":
            missing_list.append("published_date")
        if self.abstract == "":
            missing_list.append("abstract")
        if self.contents == "":
            missing_list.append("contents")
        if self.per_sections_content == "":
            missing_list.append("per_sections_content")
        if self.reference == "":
            missing_list.append("reference")
        return missing_list
