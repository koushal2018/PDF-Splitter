import os
import PyPDF2

def split_pdf(input_folder):
    # Check if the directory exists
    if not os.path.exists(input_folder):
        print(f"Error: Directory '{input_folder}' does not exist.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            print(f"Processing: {filename}")  # Print the name of the PDF being processed
            filepath = os.path.join(input_folder, filename)
            
            try:
                pdf = PyPDF2.PdfReader(filepath)
                num_pages = len(pdf.pages)

                # Create a directory to store split pages
                output_dir = os.path.join(input_folder, filename[:-4])  # remove .pdf extension
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                # Extract each page and save it as a new PDF
                for page_num in range(num_pages):
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.add_page(pdf.pages[page_num])

                    output_filename = os.path.join(output_dir, f"page_{page_num + 1}.pdf")
                    with open(output_filename, 'wb') as output_file:
                        pdf_writer.write(output_file)

                print(f"Split '{filename}' into {num_pages} pages.")
            except Exception as e:
                print(f"Error processing '{filename}': {e}")

    print("Processing completed.")

# Run the script
input_folder = "/Users/koushald/Downloads/CSDATA"  # Replace with your folder path
split_pdf(input_folder)
