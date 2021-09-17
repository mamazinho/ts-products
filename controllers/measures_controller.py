from daos.product_measure_dao import ProductMeasuresDao


class MeasuresController():

    def create_measure(self, product_id, width_value, height_value, length_value, weight_value):
        new_measure = {
            "product_id": product_id,
            "width_value": width_value,
            "height_value": height_value,
            "length_value": length_value,
            "weight_value": weight_value
        }
        measure_id = ProductMeasuresDao(new_measure).create()
        return measure_id

    def read_all_measures(self):
        list_measures = ProductMeasuresDao().read_all()
        return list_measures

    def read_by_measure_id(self, measure_id):
        measure_id = {
            'id': measure_id
        }
        measure = ProductMeasuresDao(measure_id).read_by_id()
        return measure

    def update_measure(self, measure_id, product_id, width_value, height_value, length_value, weight_value):
        measure_update = {
            "id": measure_id,
            "product_id": product_id,
            "width_value": width_value,
            "height_value": height_value,
            "length_value": length_value,
            "weight_value": weight_value
        }
        ProductMeasuresDao(measure_update).update()