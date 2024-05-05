import csv

with open('Bestseller - Sheet1.csv', 'r', encoding='utf-8') as bestseller:
    csv_reader = csv.DictReader(bestseller) # reads each row as a dictionary with column names as keys

    highestSale = 0
    bestSellingBook = None
    
    for row in csv_reader:
        
        title = row['Book']
        author = row['Author']
        
        #  handles potential conversion errors
        try:
            salesInMillions = float(row['sales in millions'])
        except ValueError:
            print(f"Skipping row due to non-numeric sales data: {title} by {author}")
            continue

        if salesInMillions > highestSale:
            highestSale = salesInMillions
            bestSellingBook = {"Title": title, "Author": author, "Sales In Millions": salesInMillions}


with open('bestseller_info.csv', 'w', newline='', encoding='utf-8') as bestsellerInfo:
    csv_writer = csv.writer(bestsellerInfo)

    csv_writer.writerow(["Book", "Author", "Sales In Millions"])

    if bestSellingBook:
        csv_writer.writerow([bestSellingBook['Title'], bestSellingBook['Author'], bestSellingBook['Sales In Millions']])
    else:
        print("No best-selling book found.")
