from orator.migrations import Migration


class CreateGoldTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('gold') as table:
            table.increments('gold_id')
            table.integer('butik_id')
            table.text('city')
            table.float('gram')
            table.float('price')
            table.float('price_per_gram')
            table.text('stock')
            table.integer('stock_int')
            table.integer('year')
            table.integer('month')
            table.integer('date')
            table.integer('origin_datetime')
            table.timestamps()

            table.index('gold_id')
            table.index('butik_id')
            table.index('gram')
            table.index('price')
            table.index('stock_int')
            table.index('year')
            table.index('month')
            table.index('date')
            table.index('origin_datetime')
            table.index('created_at')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('gold')

