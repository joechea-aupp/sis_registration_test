from main import section_parser

data = section_parser("<input type=\"checkbox\" id=\"avialable-section-3662\" class=\"validate-box selected-course\" name=\"sections[]\" value=\"3662\" data-course-id=\"635\">")

# print("<input type=\"checkbox\" id=\"avialable-section-3662\" class=\"validate-box selected-course\" name=\"sections[]\" value=\"3662\" data-course-id=\"635\">")

print(data["value"])


