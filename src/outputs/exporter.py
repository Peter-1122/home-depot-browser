thonimport json
import logging

class Exporter:
    @staticmethod
    def export_json(data, filepath):
        try:
            with open(filepath, "w") as f:
                json.dump(data, f, indent=4)
            logging.info(f"Exported JSON to {filepath}")
        except Exception as e:
            logging.error(f"Failed to export JSON: {e}")