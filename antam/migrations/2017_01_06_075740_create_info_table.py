from orator.migrations import Migration


class CreateInfoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('buy_back_info') as table:
            table.increments('buy_back_info_id')
            table.float('price')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('buy_back_info')
