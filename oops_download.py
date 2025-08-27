import os
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://cse.iitkgp.ac.in/~sourangshu/coursefiles/"

# Your HTML content (paste the entire HTML table here)
html_content = """
<tbody><tr>
      <th>Week</th>
      <th>Dates</th>
      <th>Topic / Activity</th>
      <th>Links / Material</th>
    </tr>
    <tr>
      <td>Week 1</td>
      <td>3/1, 4/1, 5/1</td>
      <td>Intro+Logistics, Recap of C, C and C++</td>
      <td><a href="se24s/intro.pdf">Slides-1</a>
      ,<a href="se24s/W1-C1-recap_c.pdf">Slides-2</a>
      ,<a href="se24s/W1-C2-C_and_C++.pdf">Slides-3</a></td>
    </tr>
    <tr>
      <td>Week 2</td>
      <td>10/1, 11/1, 12/1</td>
      <td>Constants and inline functions, Reference and pointers, Default Parameters &amp; Function Overloading, Operator overloading </td>
      <td><a href="se24s/W1-C3-constants_inline_fn.pdf">Slides-1</a>
      ,<a href="se24s/W2-C1-reference-pointer.pdf">Slides-2</a>
      ,<a href="se24s/W2-C2-default-function-overloading.pdf">Slides-3</a>
      ,<a href="se24s/W2-C3-operator-overloading.pdf">Slides-4</a></td>
    </tr>
    <tr>
      <td>Week 3</td>
      <td>17/1, 18/1, 19/1</td>
      <td>Dynamic Memory Management, Classes and objects, Access specifiers </td>
      <td><a href="se24s/W3-C1-dynamic-memory.pdf">Slides-1</a>
      ,<a href="se24s/W3-C2-classes-objects.pdf">Slides-2</a>
      ,<a href="se24s/W3-C3-access-specifiers.pdf">Slides-3</a>
    </td></tr>
    <tr>
      <td>Week 4</td>
      <td>24/1, 25/1</td>
      <td>Constructor, destructor, object lifetime, Copy Constructor and Copy Assignment Operator, Const-ness </td>
      <td><a href="se24s/W4-C1-constructor-destructor.pdf">Slides-1</a>
      ,<a href="se24s/W4-C2-copy-const-copy-assign.pdf">Slides-2</a>
      ,<a href="se24s/W4-C3-constness.pdf">Slides-3</a>
    </td></tr>
    <tr>
      <td>Week 5</td>
      <td>31/1, 1/2, 2/2</td>
      <td> Static Members, Friend Function and friend Class, Operator overloading for user defined types </td>
      <td><a href="se24s/W5-C1-static-member.pdf">Slides-1</a>
      ,<a href="se24s/W5-C2-friend.pdf">Slides-2</a>
      ,<a href="se24s/W5-C3-operator-overloading-1.pdf">Slides-3</a>
    </td></tr>
    <tr>
      <td>Week 6</td>
      <td>7/2, 8/2, 9/2</td>
      <td> Operator overloading, Namespaces, Inheritence </td>
      <td><a href="se24s/W6-C1-operator-overloading-2.pdf">Slides-1</a>
      ,<a href="se24s/W6-C2-Namespaces.pdf">Slides-2</a>
      ,<a href="se24s/W6-C3-Inheritence-1.pdf">Slides-3</a>
      ,<a href="se24s/W6-C4-Inheritence-2.pdf">Slides-4</a>
      ,<a href="se24s/W6-C5-Inheritence-3.pdf">Slides-5</a>
    </td></tr>
    <tr>
      <td>Week 7</td>
      <td>28/2, 1/3, 2/3</td>
      <td> Inheritence (Example + Private/Protected), Polymorphism (Type casting + Static / Dynamic Binding + Pure Virtual Function), 
        Example Program (Slides 6,7)</td>
      <td><a href="se24s/W7-C1-example-phonehierarchy.pdf">Slides-1</a>
      ,<a href="se24s/W7-C2-private-protected-inheritence.pdf">Slides-2</a>
      ,<a href="se24s/W7-C3-polymorphism-1.pdf">Slides-3</a>
      ,<a href="se24s/W7-C4-polymorphism-2.pdf">Slides-4</a>
      ,<a href="se24s/W7-C5-polymorphism-3.pdf">Slides-5</a>
      ,<a href="se24s/W7-C6-example-1.pdf">Slides-6</a>
      ,<a href="se24s/W7-C7-example-2.pdf">Slides-7</a>
      
    </td></tr>
    <tr>
      <td>Week 8</td>
      <td>5/3, 6/3, 7/3</td>
      <td> Virtual Function Table, Type Casting (const_cast,static_cast,reinterpret_cast,dynamic_cast), Exceptions</td>
      <td><a href="se24s/W8-C1-VFT.pdf">Slides-1</a>
      ,<a href="se24s/W8-C2-type-casting-1.pdf">Slides-2</a>
      ,<a href="se24s/W8-C2-type-casting-2.pdf">Slides-3</a>
      ,<a href="se24s/W8-C3-type-casting-3.pdf">Slides-4</a>
      ,<a href="se24s/W8-C5-multiple-inheritence.pdf">Slides-5</a>
      ,<a href="se24s/W8-C6-exceptions-1.pdf">Slides-6</a>     
    </td></tr>
    <tr>
      <td>Week 9</td>
      <td>14/3, 15/3</td>
      <td> Exceptions(Contd.), Function Templates, Class templates, Functors</td>
      <td> <a href="se24s/W9-C1-exceptions-2.pdf">Slides-1</a>
      ,<a href="se24s/W9-C2-function-template.pdf">Slides-2</a>
      ,<a href="se24s/W9-C3-class-template.pdf">Slides-3</a>
      ,<a href="se24s/W9-C4-Functor.pdf">Slides-4</a>   
    </td></tr>
    <tr>
      <td>Week 10</td>
      <td>20/3, 21/3, 22/3</td>
      <td> SDLC: Goals, Benefits, Stages, Models - waterfall, v-shaped, Spiral, Agile, UML Diagrams </td>
      <td> <a href="se24s/W10-C1-SDLC.pdf">Slides-SDLC</a>
      ,<a href="se24s/W10-C2-UML-1.pdf">Slides-UML</a>
      ,<a href="se24s/W10-C3-UML-2.pdf">Slides-Use case diagram</a>
      ,<a href="se24s/W10-C4-UML-3.pdf">Slides-class diagram</a>   
    </td></tr>
    <tr>
      <td>Week 11</td>
      <td>27/3, 28/3</td>
      <td> Software Testing </td>
      <td> <a href="se24s/W11-C1-testing.pdf">Slides-Testing</a>
    </td></tr>
    <!-- Add more rows for other weeks as needed -->
  </tbody>"""

# Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# Create main download folder
main_folder = "downloads"
os.makedirs(main_folder, exist_ok=True)

# Find all table rows (skip header)
rows = soup.find_all("tr")[1:]  # first row is header

for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 4:
        week_name = cols[0].get_text(strip=True).replace(" ", "")
        links = cols[3].find_all("a")

        # Create folder for this week
        week_folder = os.path.join(main_folder, week_name)
        os.makedirs(week_folder, exist_ok=True)

        # Download all PDFs for this week
        for link in links:
            href = link.get("href")
            if href and href.endswith(".pdf"):
                file_url = base_url + href
                file_name = os.path.basename(href)
                file_path = os.path.join(week_folder, file_name)

                print(f"Downloading {file_url} -> {file_path}")
                try:
                    response = requests.get(file_url)
                    response.raise_for_status()
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                except Exception as e:
                    print(f"Failed to download {file_url}: {e}")

print("All downloads completed week-wise!")