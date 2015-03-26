
subroutine calc_pot(pos,optpos,pot,arraylength,N,Nopt)
  implicit none
  integer, intent(in) :: N
  integer, intent(in) :: arraylength
  real(8), intent(in) :: pos(arraylength, 3)
  integer, intent(in) :: Nopt
  real(8), intent(inout) :: pot(Nopt)
  !f2py intent(in, out) pot
  real(8), intent(in) :: optpos(Nopt, 3)
  real(8) :: delta_r(3), dr2
  real(8), parameter :: rmax = 3.2_8
  integer :: i, j
  do i = 1, Nopt
  pot(i) = 0.0
    do j=1,N
      delta_r = optpos(i,:) - pos(j,:)
      dr2 = sum(delta_r**2)
      pot(i)=pot(i)+4*((1/dr2)**6 - (1/dr2)**3) 
    end do
  end do
end subroutine
