thonimport json
import logging
from pathlib import Path

from extractors.product_parser import ProductParser
from extractors.store_parser import StoreParser
from extractors.utils_query import parse_query
from outputs.exporter import Exporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    data_dir = Path(__file__).resolve().parent.parent / "data"
    query_file = data_dir / "queries.sample.txt"

    if not query_file.exists():
        logging.error("Query file not found.")
        return

    with open(query_file, "r") as f:
        queries = [line.strip() for line in f if line.strip()]

    results = []
    product_parser = ProductParser()
    store_parser = StoreParser()

    for q in queries:
        logging.info(f"Processing query: {q}")
        qtype, value = parse_query(q)

        if qtype == "product":
            results.append(product_parser.fetch_product(value))
        elif qtype == "store":
            results.append(store_parser.fetch_store(value))
        elif qtype == "keyword":
            # simulate keyword search returning one product
            fake_id = "KW-" + value.replace(" ", "-")
            results.append(product_parser.fetch_product(fake_id))
        else:
            logging.warning(f"Unknown query type for: {q}")

    output_file = data_dir / "sample_output.json"
    Exporter.export_json(results, output_file)
    logging.info(f"Results exported → {output_file}")

if __name__ == "__main__":
    main()