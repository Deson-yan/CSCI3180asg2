public class Chark extends Player {

	public Chark(int posx, int posy, int index, SurvivalGame game, boolean isHealer) {
		super(100, 4, posx, posy, index, game, isHealer);

		this.myString = "C" + Integer.toString(index);
		if (isHealer){
			this.equipment = new Wand(5,10,this);
		}
		else{
			this.equipment = new Axe(this);
		}
		this.race = "C";
	}

	public void teleport() {
		
		super.teleport();
		if (this.isHealer){
			((Wand)this.equipment).enhance();
		}
		else{
			((Axe) this.equipment).enhance();
		}
	}

	@Override
	public void askForMove() {
		// TODO Auto-generated method stub
		if (isHealer){
			System.out.println(String.format("You are a Chark (C%d) using Wand. (Range: %d, Effect: %d)",this.index,
				this.equipment.getRange(), this.equipment.getEffect()));
		}
		else{
			System.out.println(String.format("You are a Chark (C%d) using Axe. (Range: %d, Damage: %d)",this.index,
				this.equipment.getRange(), this.equipment.getEffect()));
		}
		super.askForMove();
		
	}
}
